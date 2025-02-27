# 文件：/society-management/app/models/regulation_model.py

from mongoengine import StringField
from .base_model import BaseModel

class Regulation(BaseModel):
    regulation_id = StringField(required=True, unique=True)
    regulation_name = StringField(required=True)
    regulation_content = StringField(required=True)

    meta = {
        'collection': 'regulations',
        'indexes': ['regulation_id']
    }
