from datetime import datetime
from pydantic import BaseModel, Field

class MessageBase(BaseModel):
    sender_id: str
    receiver_id: str
    content: str
    status: int = 0  # 0: 未读, 1: 已读

class MessageCreate(MessageBase):
    pass

class MessageUpdate(BaseModel):
    status: int

class MessageInDB(MessageBase):
    id: str = Field(..., alias="_id")
    sent_at: datetime

    class Config:
        allow_population_by_field_name = True