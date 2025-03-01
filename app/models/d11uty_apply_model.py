from mongoengine import StringField, IntField, DateTimeField
from .base_model import BaseModel

class DutyApply(BaseModel):
    meta = {'collection': 'duty_applies',
            'indexes': ['apply_id', 'userid']
            }
    
    apply_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    userid = StringField(required=True)
    day = DateTimeField(required=True)
    time_section = IntField(required=True)  # 1-6
def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "apply_id": self.apply_id,
            "name": self.name,
            "userid": self.userid,
            "day": self.day,
            "time_section": self.time_section,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }