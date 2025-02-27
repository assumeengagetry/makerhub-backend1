from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from loguru import logger
from app.core.db import mongodb
from app.models.c10ompetition_model import Competition

class CompetitionService:
    def __init__(self):
        self.db = mongodb.get_database()
        self.collection = self.db.competitions

    async def create_competition(self, competition: Competition) -> dict:
        try:
            competition_dict = competition.dict(exclude_unset=True)
            competition_dict["created_at"] = datetime.utcnow()
            result = await self.collection.insert_one(competition_dict)
            logger.info(f"比赛创建成功: {result.inserted_id}")
            return {"id": str(result.inserted_id)}
        except Exception as e:
            logger.error(f"创建比赛失败: {e}")
            raise

    async def get_competition(self, game_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(game_id):
            return None
        return await self.collection.find_one({"_id": ObjectId(game_id)})

    async def list_competitions(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        competitions = []
        cursor = self.collection.find(query).sort("registration_start", 1)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            competitions.append(doc)
        return competitions

    async def update_competition(self, game_id: str, game_data: dict) -> bool:
        result = await self.collection.update_one(
            {"_id": ObjectId(game_id)},
            {"$set": game_data}
        )
        return result.modified_count > 0

    async def delete_competition(self, game_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(game_id)})
        return result.deleted_count > 0