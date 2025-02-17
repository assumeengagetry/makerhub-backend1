from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.database import get_database
from app.models.games import GameModel

class CompetitionService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.games

    async def create_competition(self, game: GameModel) -> dict:
        game_dict = game.dict(exclude_unset=True)
        game_dict["created_at"] = datetime.utcnow()
        result = await self.collection.insert_one(game_dict)
        return {"id": str(result.inserted_id)}

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