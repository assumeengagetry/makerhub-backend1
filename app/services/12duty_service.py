from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import mongo
from app.models.d11uty_apply_model import DutyApply
from app.models.d12uty_model import DutyRecord

class DutyService:
    def __init__(self):
        self.db = mongo()
        self.apply_collection = self.db.duty_applies
        self.record_collection = self.db.duty_records

    async def create_duty_apply(self, apply: DutyApply) -> dict:
        apply_dict = apply.dict(exclude_unset=True)
        apply_dict["created_at"] = datetime.utcnow()
        result = await self.apply_collection.insert_one(apply_dict)
        return {"id": str(result.inserted_id)}

    async def create_duty_record(self, record: DutyRecord) -> dict:
        record_dict = record.dict(exclude_unset=True)
        record_dict["created_at"] = datetime.utcnow()
        result = await self.record_collection.insert_one(record_dict)
        return {"id": str(result.inserted_id)}

    async def get_duty_applies(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        applies = []
        cursor = self.apply_collection.find(query)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            applies.append(doc)
        return applies

    async def get_duty_records(self, user_id: str = None) -> List[dict]:
        query = {"userid": user_id} if user_id else {}
        records = []
        cursor = self.record_collection.find(query)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            records.append(doc)
        return records

    async def update_duty_record(self, record_id: str, data: dict) -> bool:
        result = await self.record_collection.update_one(
            {"_id": ObjectId(record_id)},
            {"$set": data}
        )
        return result.modified_count > 0