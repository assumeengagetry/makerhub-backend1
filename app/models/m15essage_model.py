from mongoengine import StringField, DateTimeField, IntField
from .base_model import BaseModel

class Message(BaseModel):
    meta = {
        'collection': 'messages',
        'indexes': ['message_id', 'sender_id', 'receiver_id']
    }
    
    message_id = StringField(required=True, unique=True)
    sender_id = StringField(required=True)
    receiver_id = StringField(required=True)
    content = StringField(required=True)
    sent_at = DateTimeField(required=True)
    status = IntField(default=0)  # 0: 未读, 1: 已读
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "message_id": self.message_id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "content": self.content,
            "sent_at": self.sent_at,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
