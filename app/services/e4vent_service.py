from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from loguru import logger
from app.core.db import mongodb
from app.models.e4vent_model import Event

class EventService:
    def __init__(self):
        self.db = mongodb.get_database()
        self.collection = self.db.events

    async def create_event(self, event: Event) -> dict:
        try:
            event_dict = event.dict(exclude_unset=True)
            event_dict.update({
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            })
            result = await self.collection.insert_one(event_dict)
            logger.info(f"活动创建成功: {result.inserted_id}")
            return {"id": str(result.inserted_id)}
        except Exception as e:
            logger.error(f"创建活动失败: {e}")
            raise

    async def get_event(self, event_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(event_id):
            return None
        return await self.collection.find_one({"_id": ObjectId(event_id)})

    async def list_events(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        events = []
        cursor = self.collection.find(query).sort("start_time", 1)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            events.append(doc)
        return events