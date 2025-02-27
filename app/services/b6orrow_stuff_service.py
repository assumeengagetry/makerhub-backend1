from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from loguru import logger
from app.core.db import mongodb
from app.models.b6orrow_stuff_model import BorrowRecord

class BorrowService:
    """借用服务类"""
    
    def __init__(self):
        self.db = mongodb()
        self.collection = self.db.borrows

    async def create_borrow(self, borrow: BorrowRecord) -> dict:
        """创建借用记录"""
        try:
            borrow_dict = borrow.dict(exclude_unset=True)
            borrow_dict.update({
                "created_at": datetime.utcnow(),
                "state": 0  # 未审核状态
            })
            result = await self.collection.insert_one(borrow_dict)
            return {"id": str(result.inserted_id)}
        except Exception as e:
            logger.error(f"创建借用记录失败: {e}")
            raise

    async def update_borrow_status(self, borrow_id: str, state: int) -> bool:
        """更新借用状态"""
        try:
            result = await self.collection.update_one(
                {"_id": ObjectId(borrow_id)},
                {
                    "$set": {
                        "state": state,
                        "updated_at": datetime.utcnow()
                    }
                }
            )
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"更新借用状态失败: {e}")
            raise

    async def get_borrows(self, filters: dict = None) -> List[dict]:
        """获取借用记录列表"""
        try:
            query = filters or {}
            borrows = []
            cursor = self.collection.find(query).sort("created_at", -1)
            async for doc in cursor:
                doc["id"] = str(doc["_id"])
                borrows.append(doc)
            return borrows
        except Exception as e:
            logger.error(f"获取借用记录失败: {e}")
            raise