from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import MongoDB
from app.models.s7tuff_model import Stuff

class ItemService:
    def __init__(self):
        self.db = MongoDB()
        self.stuff_collection = self.db.stuff
        self.borrow_collection = self.db.stuff_borrow

    async def add_item(self, item: Stuff) -> dict:
        item_dict = item.dict(exclude_unset=True)
        item_dict["created_at"] = datetime.utcnow()
        item_dict["updated_at"] = datetime.utcnow()
        result = await self.stuff_collection.insert_one(item_dict)
        return {"id": str(result.inserted_id)}

    async def create_borrow_request(self, request: StuffBorrowModel) -> dict:
        request_dict = request.dict(exclude_unset=True)
        request_dict["created_at"] = datetime.utcnow()
        request_dict["state"] = 0  # 未审核状态
        result = await self.borrow_collection.insert_one(request_dict)
        return {"id": str(result.inserted_id)}

    async def update_item_quantity(self, item_id: str, quantity_change: int) -> bool:
        result = await self.stuff_collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$inc": {"number": quantity_change}}
        )
        return result.modified_count > 0

    async def get_item_list(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        items = []
        cursor = self.stuff_collection.find(query)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            items.append(doc)
        return items

    async def get_borrow_records(self, user_id: str = None) -> List[dict]:
        query = {"userid": user_id} if user_id else {}
        records = []
        cursor = self.borrow_collection.find(query)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            records.append(doc)
        return records