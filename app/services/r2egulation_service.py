from typing import List, Optional
from bson import ObjectId
from app.models.r2egulation_model import Regulation
from app.core.db import mongodb

class RegulationService:
    def __init__(self):
        self.db = mongodb()
        self.collection = self.db.rules

    async def get_regulation(self, rule_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(rule_id):
            return None
        return await self.collection.find_one({"_id": ObjectId(rule_id)})