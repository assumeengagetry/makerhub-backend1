from typing import Optional
from datetime import datetime
from app.core.db import mongo
from app.core.auth import create_access_token
from loguru import logger

class UserService:
    def __init__(self):
        self.db = mongo()
        self.collection = self.db.users

    async def create_or_update_wx_user(self, openid: str, user_info: dict) -> dict:
        try:
            user = await self.collection.find_one({"userid": openid})
            if user:
                # 更新用户信息
                await self.collection.update_one(
                    {"userid": openid},
                    {"$set": user_info}
                )
            else:
                # 创建新用户
                user_info["userid"] = openid
                user_info.update({
                    "created_at": datetime.utcnow(),
                    "state": 1,
                    "score": 0,
                    "level": 1
                })
                await self.collection.insert_one(user_info)

            token = create_access_token(openid)
            return {
                "token": token,
                "user_info": await self.get_user(openid)
            }
        except Exception as e:
            logger.error(f"微信用户处理失败: {e}")
            raise e

    async def get_user(self, openid: str) -> Optional[dict]:
        return await self.collection.find_one({"userid": openid})

    async def update_user_score(self, user_id: str, score_change: int) -> bool:
        result = await self.collection.update_one(
            {"userid": user_id},
            {"$inc": {"score": score_change}}
        )
        return result.modified_count > 0

    async def update_user_state(self, user_id: str, state: int) -> bool:
        result = await self.collection.update_one(
            {"userid": user_id},
            {"$set": {"state": state}}
        )
        return result.modified_count > 0