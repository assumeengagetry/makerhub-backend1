from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import get_database
from app.models.e4vent_model import EventModel

class EventService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.events

    async def create_event(self, event: EventModel) -> dict:
        event_dict = event.dict(exclude_unset=True)
        event_dict["created_at"] = datetime.utcnow()
        event_dict["updated_at"] = datetime.utcnow()
        result = await self.collection.insert_one(event_dict)
        return {"id": str(result.inserted_id)}

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

    async def update_event(self, event_id: str, event_data: dict) -> bool:
        event_data["updated_at"] = datetime.utcnow()
        result = await self.collection.update_one(
            {"_id": ObjectId(event_id)},
            {"$set": event_data}
        )
        return result.modified_count > 0

    async def delete_event(self, event_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(event_id)})
        return result.deleted_count > 0