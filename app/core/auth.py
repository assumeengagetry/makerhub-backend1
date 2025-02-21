from datetime import datetime, timedelta
from typing import Optional
import jwt
from passlib.context import CryptContext
from fastapi import Request, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.config import settings
from app.core.db import mongo
from loguru import logger

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Token handling
def create_access_token(user_id: str, expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(user_id)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def decode_access_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload.get("sub")
    except jwt.PyJWTError:
        return None

# Authentication middleware
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

async def get_current_user(
    db: AsyncIOMotorDatabase = Depends(mongo.get_db),
    user_id: str = Depends(get_current_user_id)
):
    user = await db.users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

class AuthMiddleware:
    async def __call__(self, request: Request, call_next):
        logger.info(f"Request path: {request.url.path}")
        
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
