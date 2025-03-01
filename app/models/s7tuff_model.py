from mongoengine import Document, StringField, IntField, DateTimeField
from datetime import datetime
from .base_model import BaseModel

class Stuff(BaseModel):
    meta = {
        'collection': 'items',
        'indexes': ['stuff_id', 'type']
    }
    
    stuff_id = StringField(required=True, unique=True)
    type = StringField(required=True)
    stuff_name = StringField(required=True)
    number = IntField(default=0)
    description = StringField()
    updated_at = DateTimeField(default=datetime.now)
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "stuff_id": self.stuff_id,
            "type": self.type,
            "stuff_name": self.stuff_name,
            "number": self.number,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }