# 文件：/society-management/society-management/app/models/duty_record_model.py

from mongoengine import StringField, FloatField, DateTimeField
from .base_model import BaseModel

class DutyRecord(BaseModel):
    meta = {'collection': 'duty_records'}
    
    name = StringField(required=True)
    userid = StringField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    total = FloatField()  # 值班时长（小时）