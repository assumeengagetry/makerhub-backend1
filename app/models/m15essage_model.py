from mongoengine import Document, StringField, DateTimeField, IntField
from .base_model import BaseModel

class Message(BaseModel):
    meta = {'collection': 'messages'}
    
    sender_id = StringField(required=True)
    receiver_id = StringField(required=True)
    content = StringField(required=True)
    sent_at = DateTimeField(required=True)
    status = IntField(default=0)  # 0: 未读, 1: 已读