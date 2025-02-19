from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import mongo
from app.models.p3rinter_model import PrinterApplication

class PrinterService:
    def __init__(self):
        self.db = mongo()
        self.collection = self.db.print_requests

    async def create_print_request(self, request: PrinterApplication) -> dict:
        request_dict = request.dict(exclude_unset=True)
        request_dict["created_at"] = datetime.utcnow()
        request_dict["updated_at"] = datetime.utcnow()
        request_dict["state"] = 0  # 未审核状态
        
        result = await self.collection.insert_one(request_dict)
        return {"id": str(result.inserted_id)}

    async def update_print_status(self, request_id: str, state: int, reason: str = None) -> bool:
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

    async def get_print_request(self, request_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(request_id):
            return None
        return await self.collection.find_one({"_id": ObjectId(request_id)})

    async def list_print_requests(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        requests = []
        cursor = self.collection.find(query)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            requests.append(doc)
        return requests