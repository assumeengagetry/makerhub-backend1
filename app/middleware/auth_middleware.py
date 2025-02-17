# auth_middleware.py

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_access_token
from typing import Optional

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = None) -> Optional[str]:
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = credentials.credentials
    user_id = decode_access_token(token)
    
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid token or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user_id

async def get_current_user_id(request: Request) -> str:
    credentials = await security(request)
    return await verify_token(credentials)

class AuthMiddleware:
    async def __call__(self, request: Request, call_next):
        if request.url.path in ["/api/v1/auth/login", "/docs", "/redoc", "/openapi.json"]:
            response = await call_next(request)
            return response

        try:
            credentials = await security(request)
            user_id = await verify_token(credentials)
            request.state.user_id = user_id
        except HTTPException as e:
            return JSONResponse(
                status_code=e.status_code,
                content={"detail": str(e.detail)}
            )

        response = await call_next(request)
        return response