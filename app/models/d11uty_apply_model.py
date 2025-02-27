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
