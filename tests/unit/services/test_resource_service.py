import pytest
from app.core.db import minio_client
from unittest.mock import MagicMock

@pytest.fixture
def mock_minio(mocker):
    mock_client = mocker.patch('app.core.db.MinioClient')
    mock_client.return_value.get_file.return_value = (b"file_content", "text/plain")
    return mock_client

@pytest.mark.asyncio
async def test_get_file(mock_minio):
    file_name = "test_file.txt"
    content, content_type = await minio_client.get_file(file_name)
    assert content == b"file_content"
    assert content_type == "text/plain"
