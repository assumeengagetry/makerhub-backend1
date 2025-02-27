# 文件：/society-management/society-management/app/models/duty_record_model.py

from mongoengine import Document, StringField, FloatField, DateTimeField
from .base_model import BaseModel

class DutyRecord(BaseModel):
    meta = {'collection': 'duty_records',
            'indexes': ['record_id', 'userid']
            }
    record_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    userid = StringField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    total = FloatField()  # 值班时长（小时）
