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
    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "task_id": self.task_id,
            "department": self.department,
            "task_name": self.task_name,
            "name": self.name,
            "content": self.content,
            "state": self.state,
            "deadline": self.deadline,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
