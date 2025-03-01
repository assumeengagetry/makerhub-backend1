from typing import Optional
from app.models.u1ser_model import User
from app.core.auth import create_access_token
from loguru import logger

class UserService:
    async def create_or_update_wx_user(self, openid: str) -> dict:
        try:
            user = User.objects(userid=openid).first()
            if not user:
                # 创建新用户
                user = User(
                    userid=openid,
                    real_name="",
                    state=1,
                    score=0,
                    level=1
                )
                user.save()

            token = create_access_token(openid)
            return {
                
                "code": 200,
                "data": 
                {
                    "token": token,
                    "user_info": await self.get_user(openid),
                }
            }
        except Exception as e:
            logger.error(f"微信用户处理失败: {e}")
            raise e

    async def get_user(self, openid: str) -> Optional[dict]:
        user = User.objects(userid=openid).first()
        return user.to_dict() if user else None

    async def update_user_score(self, user_id: str, score_change: int) -> bool:
        try:
            user = User.objects(userid=user_id).first()
            if user:
                user.score += score_change
                user.save()
                return True
            return False
        except Exception:
            return False

    async def update_user_state(self, user_id: str, state: int) -> bool:
        try:
            user = User.objects(userid=user_id).first()
            if user:
                user.state = state
                user.save()
                return True
            return False
        except Exception:
            return False
        
    async def update_user_realname(self, user_id: str, real_name: str) -> bool:
        try:
            user = User.objects(userid=user_id).first()
            if user:
                user.real_name = real_name
                user.save()
                return True
            return False
        except Exception:
            return False