import pytest
from app.services.b6orrow_stuff_service import BorrowService
from app.models.b6orrow_stuff_model import BorrowRecord
from unittest.mock import MagicMock
from datetime import datetime

@pytest.fixture
def mock_mongo(mocker):
    mock_db = mocker.patch('app.core.db.mongo')
    mock_collection = MagicMock()
    mock_db.return_value.borrows = mock_collection
    return mock_collection

@pytest.mark.asyncio
async def test_create_borrow(mock_mongo):
    borrow_service = BorrowService()
    borrow_data = BorrowRecord(
        sb_id="12345",
        userid="user_001",
        name="John Doe",
        phone_num="1234567890",
        email="john.doe@example.com",
        grade="A",
        major="CS",
        project_num="proj_001",
        type="Personal",
        stuff_name="Laptop",
        stuff_quantity_change=1,
        deadline=datetime(2025, 12, 31),
        reason="Need for project",
        categories=0
    )
    
    # Mock the database insert operation
    mock_mongo.insert_one.return_value.inserted_id = "some_id"
    
    response = await borrow_service.create_borrow(borrow_data)
    
    assert response["id"] == "some_id"

@pytest.mark.asyncio
async def test_update_borrow_status(mock_mongo):
    borrow_service = BorrowService()
    borrow_id = "some_id"
    
    # Mock the database update operation
    mock_mongo.update_one.return_value.modified_count = 1
    
    response = await borrow_service.update_borrow_status(borrow_id, state=1)
    
    assert response is True

@pytest.mark.asyncio
async def test_get_borrows(mock_mongo):
    borrow_service = BorrowService()
    filters = {"userid": "user_001"}
    
    # Mock the database find operation
    mock_mongo.find.return_value = [
        {"sb_id": "12345", "userid": "user_001", "stuff_name": "Laptop"}
    ]
    
    borrows = await borrow_service.get_borrows(filters)
    assert len(borrows) == 1
    assert borrows[0]["sb_id"] == "12345"
