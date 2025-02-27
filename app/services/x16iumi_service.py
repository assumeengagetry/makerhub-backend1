from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.core.db import mongodb  # 使用统一的数据库连接
from app.models.x16iumi_model import XiumiLink
from loguru import logger

class XiumiService:
    def __init__(self):
        self.db = mongodb.get_database()
        self.collection = self.db.publicity_links

    async def create_link(self, link: XiumiLink) -> dict:
        try:
            link_dict = link.dict(exclude_unset=True)
            link_dict.update({
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            })
            result = await self.collection.insert_one(link_dict)
            logger.info(f"宣传链接创建成功: {result.inserted_id}")
            return {"id": str(result.inserted_id)}
        except Exception as e:
            logger.error(f"创建宣传链接失败: {e}")
            raise

    async def get_links(self, filters: dict = None) -> List[dict]:
        query = filters or {}
        links = []
        cursor = self.collection.find(query).sort("created_at", -1)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            links.append(doc)
        return links

    async def delete_link(self, link_id: str) -> bool:
        if not ObjectId.is_valid(link_id):
            return False
        result = await self.collection.delete_one({"_id": ObjectId(link_id)})
        return result.deleted_count > 0

    async def get_user_links(self, userid: str) -> List[dict]:
        return await self.get_links({"userid": userid})