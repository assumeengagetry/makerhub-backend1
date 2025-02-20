# tests/unit/services/test_user_service.py
import pytest
from app.services.u1ser_service import UserService
from app.models.u1ser_model import User

@pytest.mark.asyncio
async def test_create_user(test_db):
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepass"
    }
    
    created_user = await UserService.create_user(user_data)
    
    assert created_user.username == "testuser"
    assert "password" not in created_user.dict()
    assert await test_db.users.find_one({"username": "testuser"})