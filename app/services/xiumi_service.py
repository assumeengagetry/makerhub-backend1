from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from app.database import get_database
from app.models.publicity_link import PublicityLinkModel

class XiumiService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.publicity_links

    async def create_link(self, link: PublicityLinkModel) -> dict:
        link_dict = link.dict(exclude_unset=True)
        link_dict["created_at"] = datetime.utcnow()
        result = await self.collection.insert_one(link_dict)
        return {"id": str(result.inserted_id)}

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