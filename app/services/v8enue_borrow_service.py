from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import mongodb
from app.models.v8enue_borrow_model import VenueBorrow

class VenueService:
    def __init__(self):
        self.db = mongodb()
        self.collection = self.db.site_borrows

    async def create_venue_request(self, request: VenueBorrow) -> dict:
        request_dict = request.dict(exclude_unset=True)
        request_dict.update({
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "state": 0  # 待审核
        })
        result = await self.collection.insert_one(request_dict)
        return {"id": str(result.inserted_id)}

    async def update_venue_status(self, request_id: str, state: int, reason: str = None) -> bool:
        update_data = {
            "state": state,
            "updated_at": datetime.utcnow()
        }
        if reason:
            update_data["reason"] = reason
            
        result = await self.collection.update_one(
            {"_id": ObjectId(request_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    async def get_venue_requests(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        requests = []
        cursor = self.collection.find(query).sort("start_time", 1)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            requests.append(doc)
        return requests

    async def get_venue_request(self, apply_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(apply_id):
            return None
        doc = await self.collection.find_one({"_id": ObjectId(apply_id)})
        if doc:
            doc["id"] = str(doc["_id"])
        return doc