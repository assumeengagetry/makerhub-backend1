import pytest
from app.models.user_model import User

def test_create_member():
    member = User(
        name="测试用户",
        student_id="2021000001",
        department="创新部"
    )
    assert member.name == "测试用户"
    assert member.student_id == "2021000001"

def test_update_member():
    member = User(
        name="测试用户",
        student_id="2021000001",
        department=""
    )
    member.department = ""
    assert member.department == ""