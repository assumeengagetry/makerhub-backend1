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
    def to_dict(self):
        """转换为字典格式"""
        return {
            "id": str(self.id),
            "apply_id": self.apply_id,
            "project_name": self.project_name,
            "director": self.director,
            "college": self.college,
            "major_grade": self.major_grade,
            "phone_num": self.phone_num,
            "email": self.email,
            "mentor": self.mentor,
            "description": self.description,
            "application_file": self.application_file,
            "prove_file": self.prove_file,
            "member": self.member,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "audit_state": self.audit_state,
            "project_state": self.project_state,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
