# 文件：/society-management/society-management/app/models/item_model.py

from mongoengine import Document, StringField, IntField, DateTimeField
from datetime import datetime
from .base_model import BaseModel

class Item(BaseModel):
    meta = {'collection': 'items'}
    
    stuff_id = StringField(required=True, unique=True)
    type = StringField(required=True)
    stuff_name = StringField(required=True)
    number = IntField(default=0)
    description = StringField()
    updated_at = DateTimeField(default=datetime.now)