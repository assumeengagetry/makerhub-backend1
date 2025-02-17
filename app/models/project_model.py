from mongoengine import StringField, IntField, ListField, DateTimeField
from .base_model import BaseModel

class Project(BaseModel):
    apply_id = StringField(required=True, unique=True)
    project_name = StringField(required=True)
    director = StringField(required=True)
    college = StringField(required=True)
    major_grade = StringField(required=True)
    phone_num = StringField(required=True)
    email = StringField(required=True)
    mentor = StringField(required=True)
    description = StringField()
    application_file = StringField()  # Base64编码文件
    prove_file = StringField()  # Base64编码文件
    member = ListField(StringField())
    start_time = DateTimeField()
    end_time = DateTimeField()
    audit_state = IntField(default=0)  # 0：待审核，1：通过，2：拒绝
    project_state = IntField(default=1)  # 0：已结束，1：进行中

    meta = {
        'collection': 'projects',
        'indexes': ['apply_id', 'project_name']
    }