# 文件：/society-management/society-management/app/models/event_model.py

from mongoengine import StringField, DateTimeField
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