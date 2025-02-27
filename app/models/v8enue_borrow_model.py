from mongoengine import StringField, IntField, DateTimeField
from .base_model import BaseModel

class VenueBorrow(BaseModel):
    apply_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    student_id = StringField(required=True)
    phonenum = StringField(required=True)
    email = StringField(required=True)
    purpose = StringField(required=True)
    mentor_name = StringField()
    mentor_phone_num = StringField()
    picture = StringField()  # base64编码
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    state = IntField(default=0)  # 0: 待审核，1: 审核通过，2: 审核未通过
    reason = StringField()

    meta = {
        'collection': 'venue_borrows',
        'indexes': ['apply_id', 'student_id']
    }
