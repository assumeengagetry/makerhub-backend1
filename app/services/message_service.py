from typing import List
from datetime import datetime
from bson import ObjectId
from app.database import get_database
from app.models.messages import MessageModel

class MessageService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.messages

    async def send_message(self, message: MessageModel) -> dict:
        message_dict = message.dict(exclude_unset=True)
        message_dict["sent_at"] = datetime.utcnow()
        message_dict["status"] = "unread"
        
        result = await self.collection.insert_one(message_dict)
        return {"id": str(result.inserted_id)}

    async def get_user_messages(self, user_id: str, status: str = None) -> List[dict]:
        query = {"receiver_id": user_id}
        if status:
            query["status"] = status
        
        messages = []
        cursor = self.collection.find(query).sort("sent_at", -1)
        async for doc in cursor:
            doc["id"] = str(doc["_id"])
            messages.append(doc)
        return messages

    async def mark_as_read(self, message_id: str) -> bool:
        result = await self.collection.update_one(
            {"_id": ObjectId(message_id)},
            {"$set": {"status": "read"}}
        )
        return result.modified_count > 0

    async def delete_message(self, message_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(message_id)})
        return result.deleted_count > 0