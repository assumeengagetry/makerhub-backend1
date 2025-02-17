# 文件：/society-management/society-management/app/models/regulation_model.py

from mongoengine import StringField
from .base_model import BaseModel

class Regulation(BaseModel):
    file_id = StringField(required=True, unique=True)
    file_name = StringField(required=True)
    content = StringField(required=True)

    meta = {
        'collection': 'regulations',
        'indexes': ['file_id']
    }