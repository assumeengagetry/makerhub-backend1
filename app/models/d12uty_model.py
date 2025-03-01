# 文件：/society-management/society-management/app/models/duty_record_model.py

from mongoengine import Document, StringField, FloatField, DateTimeField
from .base_model import BaseModel

class DutyRecord(BaseModel):
    meta = {
        'collection': 'duty_records',
        'indexes': ['record_id', 'userid']
    }
    
    record_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    userid = StringField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    total = FloatField()  # 值班时长（小时）
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "record_id": self.record_id,
            "name": self.name,
            "userid": self.userid,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "total": self.total,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }