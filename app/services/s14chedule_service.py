from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import mongo
from app.models.s14chedule_model import Schedule

class ScheduleService:
    def __init__(self):
        self.db = mongo()
        self.collection = self.db.arrangements

    async def create_schedule(self, schedule: Schedule) -> dict:
        schedule_dict = schedule.dict(exclude_unset=True)
        schedule_dict["created_at"] = datetime.utcnow()
        result = await self.collection.insert_one(schedule_dict)
        return {"id": str(result.inserted_id)}

    async def update_schedule(self, schedule_id: str, data: dict) -> bool:
        result = await self.collection.update_one(
            {"_id": ObjectId(schedule_id)},
            {"$set": data}
        )
        return result.modified_count > 0

    async def get_schedules(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        schedules = []
        cursor = self.collection.find(query).sort("order", 1)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            schedules.append(doc)
        return schedules