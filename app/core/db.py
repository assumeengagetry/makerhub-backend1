from motor.motor_asyncio import AsyncIOMotorClient
from minio import Minio
from minio.error import S3Error
from fastapi import HTTPException, Depends, status
from app.core.config import settings
from loguru import logger
import io
from typing import AsyncGenerator

# MongoDB client
class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

    async def connect_to_database(self):
        try:
            logger.info("正在连接到MongoDB...")
            self.client = AsyncIOMotorClient(settings.MONGO_URI)
            self.db = self.client[settings.MONGO_DB]
            logger.info("MongoDB连接成功")
        except Exception as e:
            logger.error(f"连接MongoDB失败: {e}")

    async def close_database_connection(self):
        try:
            logger.info("正在关闭MongoDB连接...")
            if self.client:
                self.client.close()
                logger.info("MongoDB连接已关闭")
        except Exception as e:
            logger.error(f"关闭MongoDB连接失败: {e}")

    async def create_indexes(self):
        try:
            logger.info("正在创建MongoDB索引...")
            await self.db.users.create_index("userid", unique=True)
            await self.db.duty_records.create_index("userid")
            await self.db.borrow_records.create_index("apply_id", unique=True)
            logger.info("MongoDB索引创建完成")
        except Exception as e:
            logger.error(f"创建MongoDB索引失败: {e}")

    async def get_db(self) -> AsyncGenerator:
        try:
            yield self.db
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    def get_collection(self, collection_name: str):
        async def get_collection_dependency(db = Depends(self.get_db)):
            return db[collection_name]
        return get_collection_dependency

# MinIO client
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

# Initialize clients
mongo = MongoDB()
minio_client = MinioClient()
