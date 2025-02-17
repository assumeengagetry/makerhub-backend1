import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def test_db():
    # 使用测试数据库配置
    settings.MONGODB_DATABASE = "test_society_db"
    yield
    # 清理测试数据库