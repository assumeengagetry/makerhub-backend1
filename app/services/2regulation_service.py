from typing import List, Optional
from bson import ObjectId
from app.models.r2egulation_model import Regulation
from app.core.db import mongo

class RegulationService:
    def __init__(self):
        self.db = mongo()
        self.collection = self.db.rules

    async def create_regulation(self, rule: Regulation) -> dict:
        result = await self.collection.insert_one(rule.dict(exclude_unset=True))
        return {"id": str(result.inserted_id)}

    async def get_regulation(self, rule_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(rule_id):
            return None
        return await self.collection.find_one({"_id": ObjectId(rule_id)})

    async def list_regulations(self) -> List[dict]:
        regulations = []
        cursor = self.collection.find({})
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            regulations.append(doc)
        return regulations

    async def update_regulation(self, rule_id: str, rule_data: dict) -> bool:
        if not ObjectId.is_valid(rule_id):
            return False
        result = await self.collection.update_one(
            {"_id": ObjectId(rule_id)},
            {"$set": rule_data}
        )
        return result.modified_count > 0

    async def delete_regulation(self, rule_id: str) -> bool:
        if not ObjectId.is_valid(rule_id):
            return False
        result = await self.collection.delete_one({"_id": ObjectId(rule_id)})
        return result.deleted_count > 0