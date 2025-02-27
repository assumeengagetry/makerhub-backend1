from mongoengine import StringField, IntField
from .base_model import BaseModel

class Schedule(BaseModel):
    name = StringField(required=True)
    type = StringField(required=True)  # 工作类型
    order = IntField(required=True)  # 工作顺序

    meta = {
        'collection': 'schedules',
        'indexes': ['name', 'type']
    }
