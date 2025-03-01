from mongoengine import StringField
from app.models.base_model import BaseModel

class XiumiLink(BaseModel):
    """秀米链接模型"""
    
    meta = {
        'collection': 'publicity_links',
        'indexes': ['userid']
    }
    
    name = StringField(required=True)  # 提交人姓名
    userid = StringField(required=True)  # 用户ID
    link = StringField(required=True)  # 秀米链接

    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "name": self.name,
            "userid": self.userid,
            "link": self.link,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
