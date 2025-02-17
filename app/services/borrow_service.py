from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.database import get_database
from app.models.stuff_borrow import StuffBorrowModel

class BorrowService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.borrows

    async def create_borrow(self, borrow: StuffBorrowModel) -> dict:
        borrow_dict = borrow.dict(exclude_unset=True)
        borrow_dict.update({
            "created_at": datetime.utcnow(),
            "state": 0  # 未审核状态
        })
        result = await self.collection.insert_one(borrow_dict)
        return {"id": str(result.inserted_id)}

    async def update_borrow_status(self, borrow_id: str, state: int) -> bool:
        result = await self.collection.update_one(
            {"_id": ObjectId(borrow_id)},
            {"$set": {
                "state": state,
                "updated_at": datetime.utcnow()
            }}
        )
        return result.modified_count > 0

    async def get_borrows(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        borrows = []
        cursor = self.collection.find(query)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            borrows.append(doc)
        return borrows