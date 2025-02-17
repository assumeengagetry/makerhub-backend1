from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.database import get_database
from app.models.user import UserModel

class UserService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.users

    async def create_user(self, user: UserModel) -> dict:
        user_dict = user.dict(exclude_unset=True)
        user_dict.update({
            "created_at": datetime.utcnow(),
            "state": 1,  # 正常状态
            "score": 0   # 初始积分
        })
        result = await self.collection.insert_one(user_dict)
        return {"id": str(result.inserted_id)}

    async def get_user(self, user_id: str) -> Optional[dict]:
        return await self.collection.find_one({"userid": user_id})

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