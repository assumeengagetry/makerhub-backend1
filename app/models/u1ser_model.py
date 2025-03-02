from mongoengine import StringField, IntField, BinaryField
from .base_model import BaseModel

class User(BaseModel):
    userid = StringField(required=True, unique=True)  # 使用微信openid作为用户ID
    level = IntField(default=1)  # 0：普通用户，1：干事，2：部长及以上
    real_name = StringField(required=False)
    phone_num = StringField()
    state = IntField(default=1)  # 0：封禁，1：正常
    profile_photo = BinaryField()
    score = IntField(default=0)

    meta = {
        'collection': 'users',
        'indexes': ['userid', 'phone_num', 'real_name', 'level', 'state']
    }
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            "userid": self.userid,
            "level": self.level,
            "real_name": self.real_name,
            "phone_num": self.phone_num,
            "state": self.state,
            "profile_photo": self.profile_photo,
            "score": self.score,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }