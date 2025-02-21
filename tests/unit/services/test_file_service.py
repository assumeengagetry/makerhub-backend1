# tests/unit/services/test_file_service.py
from unittest.mock import Mock
from app.services.x16iumi_service import XiumiService
import pytest
from app.core.config import settings

@pytest.fixture
def mock_minio():
    mock = Mock()
    mock.put_object.return_value = "success"
    return mock

def test_upload_file(mock_minio):
    service = XiumiService(minio_client=mock_minio)
    result = service.upload_file(b"test", "test.txt")
    
    assert result == "success"
    mock_minio.put_object.assert_called_once_with(
        bucket_name=settings.MINIO_BUCKET_NAME,
        object_name="test.txt",
        data=b"test"
    )