from typing import List
from app.models.m15essage_model import Message

class MessageService:
    async def send_message(self, message_data: dict) -> dict:
        message = Message(**message_data)
        message.status = "unread"
        message.save()
        return {"id": str(message.id)}

    async def get_user_messages(self, user_id: str, status: str = None) -> List[dict]:
        query = {"receiver_id": user_id}
        if status:
            query["status"] = status
        
        messages = Message.objects(**query).order_by("-sent_at")
        return [message.to_dict() for message in messages]

    async def mark_as_read(self, message_id: str) -> bool:
        try:
            message = Message.objects.get(id=message_id)
            message.status = "read"
            message.save()
            return True
        except Message.DoesNotExist:
            return False

    async def delete_message(self, message_id: str) -> bool:
        try:
            message = Message.objects.get(id=message_id)
            message.delete()
            return True
        except Message.DoesNotExist:
            return False