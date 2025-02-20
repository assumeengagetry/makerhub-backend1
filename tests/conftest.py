import pytest
from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient
from app.main import app
from app.core.config import settings
from app.core.db import mongo
import os

@pytest.fixture(scope="module")
def test_db():
    # 使用测试专用数据库
    original_db = settings.MONGO_DB
    settings.MONGO_DB = "test_db"
    client = AsyncIOMotorClient(settings.MONGO_URI)
    yield client[settings.MONGO_DB]
    # 测试结束后清理数据库
    client.drop_database(settings.MONGO_DB)
    settings.MONGO_DB = original_db

@pytest.fixture(scope="module")
def test_client(test_db):
    # 覆盖数据库依赖
    app.dependency_overrides[mongo] = lambda: test_db
    with TestClient(app) as client:
        yield client

@pytest.fixture
def test_user(test_client):
    # 创建测试用户
    user_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    response = test_client.post("/api/users/", json=user_data)
    return response.json()