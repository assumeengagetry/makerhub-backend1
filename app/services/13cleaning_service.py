from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import mongo
from app.models.c13leaning_model import CleaningRecord

class CleaningService:
    def __init__(self):
        self.db = mongo()
        self.collection = self.db.cleaning_records

    async def create_cleaning_record(self, record: CleaningRecord) -> dict:
        record_dict = record.dict(exclude_unset=True)
        record_dict["created_at"] = datetime.utcnow()
        record_dict["updated_at"] = datetime.utcnow()
        result = await self.collection.insert_one(record_dict)
        return {"id": str(result.inserted_id)}

    async def get_cleaning_records(self, user_id: str = None) -> List[dict]:
        query = {"userid": user_id} if user_id else {}
        records = []
        cursor = self.collection.find(query)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            records.append(doc)
        return records

    async def update_cleaning_times(self, record_id: str, times: int) -> bool:
        result = await self.collection.update_one(
            {"_id": ObjectId(record_id)},
            {
                "$set": {
                    "times": times,
                    "updated_at": datetime.utcnow()
                }
            }
        )
        return result.modified_count > 0