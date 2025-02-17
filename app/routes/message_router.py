from fastapi import APIRouter, HTTPException
from app.models.messages_model import Message
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class MessageCreate(BaseModel):
    sender_id: str
    receiver_id: str
    content: str

@router.post("/message")
async def send_message(message: MessageCreate):
    new_message = await Message(
        **message.dict(),
        sent_at=datetime.now(),
        status="unread"
    ).save()
    return {"message": "消息发送成功", "id": str(new_message.id)}

@router.get("/messages/{user_id}")
async def get_user_messages(user_id: str):
    messages = await Message.objects(receiver_id=user_id).all()
    return [msg.dict() for msg in messages]