from datetime import datetime, timedelta
from typing import Optional
import jwt
from fastapi import Request, HTTPException, Header, Depends
from fastapi.security import HTTPBearer
from app.core.config import settings
from app.models.u1ser_model import User
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
    NO_AUTH_PATHS = {
        "/api/v1/users/wx-login",
        "/api/docs",
        "/api/redoc",
        "/api/openapi.json",
        "/health",
    }


    @classmethod
    async def get_current_user(cls, token: str = Header(..., alias="Authorization")) -> User:
        try:
            if token.startswith("Bearer "):
                token = token.split(" ")[1]
            userid = decode_token(token)
            user = User.__objects(userid=userid).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user
        except Exception as e:
            logger.error(f"Auth error: {e}")
            raise HTTPException(status_code=401, detail="Authentication failed")

    async def __call__(self, request: Request, call_next):
        if self.NO_AUTH_PATHS.intersection({request.url.path}):
            return await call_next(request)

        try:
            token = request.headers.get("Authorization")
            user = await self.get_current_user(token)
            request.state.user = user
            return await call_next(request)
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"认证错误: {str(e)}")
            raise HTTPException(status_code=401, detail="认证失败")

def require_permission_level(required_level: int):
    """权限等级要求装饰器"""
    
    async def check_permission_level(
        auth_level: int = Depends(AuthMiddleware.get_current_user)
    ):
        if auth_level.level < required_level:
            raise HTTPException(
                status_code=403,
                detail=f"需要权限等级 {required_level}, 当前等级 {auth_level.level}"
            )
        return auth_level
    return check_permission_level

# 便捷的权限检查装饰器
require_admin = require_permission_level(settings.PERMISSION_LEVELS["ADMIN"])
require_super = require_permission_level(settings.PERMISSION_LEVELS["SUPER"])

