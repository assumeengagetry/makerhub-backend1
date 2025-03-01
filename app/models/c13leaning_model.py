from mongoengine import Document, StringField, IntField, DateTimeField
from datetime import datetime
from .base_model import BaseModel

class CleaningRecord(BaseModel):
    meta = {'collection': 'cleaning_records',
            'indexes': ['record_id', 'userid']
            }
    
    record_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    userid = StringField(required=True)
    times = IntField(default=0)
    updated_at = DateTimeField(default=datetime.now)

def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "record_id": self.record_id,
            "name": self.name,
            "userid": self.userid,
            "times": self.times,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }