from minio import Minio
from minio.error import S3Error
from fastapi import HTTPException
from app.core.config import settings
import io

class MinioClient:
    def __init__(self):
        self.client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=False
        )
        self._ensure_bucket_exists()
    
    def _ensure_bucket_exists(self):
        try:
            if not self.client.bucket_exists(settings.MINIO_BUCKET):
                self.client.make_bucket(settings.MINIO_BUCKET)
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"MinIO error: {str(e)}")
    
    def upload_file(self, file_data: bytes, filename: str, content_type: str) -> str:
        try:
            self.client.put_object(
                settings.MINIO_BUCKET,
                filename,
                io.BytesIO(file_data),
                len(file_data),
                content_type
            )
            return f"{settings.MINIO_ENDPOINT}/{settings.MINIO_BUCKET}/{filename}"
        except S3Error as e:
            raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")
    
    def get_file(self, filename: str) -> tuple[bytes, str]:
        try:
            data = self.client.get_object(settings.MINIO_BUCKET, filename)
            return data.read(), data.info().get("Content-Type", "application/octet-stream")
        except S3Error as e:
            raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

minio_client = MinioClient()