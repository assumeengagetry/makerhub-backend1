from mongoengine import StringField
from .base_model import BaseModel

class XiumiLink(BaseModel):
    name = StringField(required=True)
    userid = StringField(required=True)  # 提交人邮箱
    link = StringField(required=True)

    meta = {
        'collection': 'xiumi_links',
        'indexes': ['userid']
    }