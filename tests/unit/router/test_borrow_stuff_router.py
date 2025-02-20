from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_borrow_request():
    response = client.post(
        "/api/v1/borrow_stuff/borrow",
        json={
            "sb_id": "12345",
            "userid": "user_001",
            "name": "John Doe",
            "phone_num": "1234567890",
            "email": "john.doe@example.com",
            "grade": "A",
            "major": "CS",
            "project_num": "proj_001",
            "type": "Personal",
            "stuff_name": "Laptop",
            "stuff_quantity_change": 1,
            "deadline": "2025-12-31",
            "reason": "Need for project",
            "categories": 0
        }
    )
    
    assert response.status_code == 200
    assert response.json() == {"message": "借用申请创建成功", "id": "some_id"}

def test_update_borrow_status():
    response = client.put(
        "/api/v1/borrow_stuff/borrow/12345",
        json={"state": 1}
    )
    
    assert response.status_code == 200
    assert response.json() == {"message": "借用申请状态更新成功"}

def test_get_user_borrows():
    response = client.get("/api/v1/borrow_stuff/borrows/user_001")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
