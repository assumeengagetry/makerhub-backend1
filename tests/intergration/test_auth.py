# tests/integration/test_auth.py
def test_login_flow(test_client, test_user):
    # 测试登录失败场景
    wrong_creds = {
        "username": "testuser",
        "password": "wrongpassword"
    }
    response = test_client.post("/api/auth/login", data=wrong_creds)
    assert response.status_code == 401
    
    # 测试登录成功
    valid_creds = {
        "username": "testuser",
        "password": "testpass123"
    }
    response = test_client.post("/api/auth/login", data=valid_creds)
    assert response.status_code == 200
    assert "access_token" in response.json()