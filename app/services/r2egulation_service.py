from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import mongodb
from app.models.r2egulation_model import Regulation

class RegulationService:
    def __init__(self):
        self.db = mongodb.get_database()
        self.collection = self.db.regulations

    async def get_regulation(self, regulation_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(regulation_id):
            return None
        doc = await self.collection.find_one({"_id": ObjectId(regulation_id)})
        if doc:
            doc["id"] = str(doc["_id"])
        return doc