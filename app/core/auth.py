from datetime import datetime, timedelta
from typing import Optional
import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from app.core.config import settings
from loguru import logger

security = HTTPBearer()

def create_access_token(openid: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(openid)}
    return jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)

def decode_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload.get("sub")
    except jwt.PyJWTError:
        return None

class AuthMiddleware:
    async def __call__(self, request: Request, call_next):
        if request.url.path in [
            "/api/v1/users/wx-login",
            "/api/docs",
            "/api/redoc",
            "/api/openapi.json",
            "/health"
        ]:
            return await call_next(request)

        try:
            auth = request.headers.get("Authorization")
            if not auth:
                raise HTTPException(status_code=401, detail="未提供认证信息")
            
            scheme, token = auth.split()
            if scheme.lower() != "bearer":
                raise HTTPException(status_code=401, detail="无效的认证方案")
            
            openid = decode_token(token)
            if not openid:
                raise HTTPException(status_code=401, detail="无效的令牌")
            
            request.state.user_id = openid
            return await call_next(request)
        except Exception as e:
            logger.error(f"认证错误: {str(e)}")
            raise HTTPException(status_code=401, detail="认证失败")
