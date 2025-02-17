from mongoengine import StringField, IntField, DateTimeField
from .base_model import BaseModel

class Task(BaseModel):
    task_id = StringField(required=True, unique=True)
    department = StringField(required=True)
    task_name = StringField(required=True)
    name = StringField(required=True)
    content = StringField()
    state = IntField(default=0)  # 0: 未完成，1: 已完成
    deadline = DateTimeField()

    meta = {
        'collection': 'tasks',
        'indexes': ['task_id', 'department']
    }