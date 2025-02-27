from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import mongodb
from app.models.s7tuff_model import Stuff
from app.models.b6orrow_stuff_model import BorrowRecord

class StuffService:
    def __init__(self):
        self.db = mongodb.get_database()
        self.collection = self.db.stuff

    async def add_item(self, stuff: Stuff) -> dict:
        stuff_dict = stuff.dict(exclude_unset=True)
        stuff_dict.update({
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        })
        result = await self.collection.insert_one(stuff_dict)
        return {"id": str(result.inserted_id)}

    async def update_item_quantity(self, stuff_id: str, new_quantity: int) -> bool:
        if not ObjectId.is_valid(stuff_id):
            return False
        result = await self.collection.update_one(
            {"_id": ObjectId(stuff_id)},
            {"$set": {
                "number": new_quantity,
                "updated_at": datetime.utcnow()
            }}
        )
        return result.modified_count > 0

    async def get_item_list(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        items = []
        cursor = self.collection.find(query).sort("created_at", -1)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            items.append(doc)
        return items

    async def create_borrow_request(self, request: BorrowRecord) -> dict:
        request_dict = request.dict(exclude_unset=True)
        request_dict["created_at"] = datetime.utcnow()
        request_dict["state"] = 0  # 未审核状态
        result = await self.borrow_collection.insert_one(request_dict)
        return {"id": str(result.inserted_id)}

    async def get_borrow_records(self, user_id: str = None) -> List[dict]:
        query = {"userid": user_id} if user_id else {}
        records = []
        cursor = self.borrow_collection.find(query)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            records.append(doc)
        return records