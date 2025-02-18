from mongoengine import StringField, IntField, BinaryField
from .base_model import BaseModel

class User(BaseModel):
    userid = StringField(required=True, unique=True)  # 邮箱作为用户ID
    password = StringField(required=True)
    level = IntField(default=1)  # 1：编外人员，2：干事，3：部长及以上
    real_name = StringField(required=True)
    phone_num = StringField()
    note = StringField()
    state = IntField(default=1)  # 0：封禁，1：正常
    profile_photo = BinaryField()
    score = IntField(default=0)

    meta = {
        'collection': 'users',
        'indexes': ['userid', 'phone_num','real_name','email'] # 字段创建索引
    }