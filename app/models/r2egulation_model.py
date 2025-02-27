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
    def to_dict(self):
        return {
            "regulation_id": self.regulation_id,
            "regulation_name": self.regulation_name,
            "regulation_content": self.regulation_content,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }