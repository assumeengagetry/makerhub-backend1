from mongoengine import StringField, IntField, BinaryField
from .base_model import BaseModel

class User(BaseModel):
    userid = StringField(required=True, unique=True)  # 使用微信openid作为用户ID
    level = IntField(default=1)  # 0：普通用户，1：干事，2：部长及以上
    real_name = StringField(required=True)
    phone_num = StringField()
    state = IntField(default=1)  # 0：封禁，1：正常
    profile_photo = BinaryField()
    score = IntField(default=0)

    meta = {
        'collection': 'users',
        'indexes': ['userid', 'phone_num', 'real_name', 'level', 'state']
    }
    def to_dict(self):
        return {
            "userid": self.userid,
            "phone": self.phone_num,
            "permission_level": self.level,
        }