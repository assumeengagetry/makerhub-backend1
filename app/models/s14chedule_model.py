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
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "name": self.name,
            "type": self.type,
            "order": self.order,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }