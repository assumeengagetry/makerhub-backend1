def test_borrow_request_flow():
    # 模拟用户创建借用请求
    response_create = client.post("/api/v1/borrow_stuff/borrow", json={
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
    })
    borrow_id = response_create.json()["id"]

    # 模拟管理员更新借用请求状态
    response_update = client.put(f"/api/v1/borrow_stuff/borrow/{borrow_id}", json={"state": 1})
    assert response_update.status_code == 200
    assert response_update.json() == {"message": "借用申请状态更新成功"}
    
    # 模拟用户查询借用记录
    response_get = client.get(f"/api/v1/borrow_stuff/borrows/user_001")
    assert response_get.status_code == 200
    assert len(response_get.json()) > 0
