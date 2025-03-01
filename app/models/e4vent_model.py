# 文件：/society-management/society-management/app/models/event_model.py

from mongoengine import Document, StringField, DateTimeField
from .base_model import BaseModel

class Event(BaseModel):
    event_id = StringField(required=True, unique=True)
    event_name = StringField(required=True)
    poster = StringField()  # base64编码的图片
    description = StringField()
    location = StringField()
    link = StringField()
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    registration_deadline = DateTimeField()

    meta = {
        'collection': 'events',
        'indexes': ['event_id', 'event_name']
    }
    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "event_id": self.event_id,
            "event_name": self.event_name,
            "poster": self.poster,
            "description": self.description,
            "location": self.location,
            "link": self.link,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "registration_deadline": self.registration_deadline,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

