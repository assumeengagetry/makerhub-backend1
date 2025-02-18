from mongoengine import Document, StringField, IntField, DateTimeField
from datetime import datetime
from .base_model import BaseModel

class CleaningRecord(BaseModel):
    meta = {'collection': 'cleaning_records'}
    
    record_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    userid = StringField(required=True)
    times = IntField(default=0)
    updated_at = DateTimeField(default=datetime.now)