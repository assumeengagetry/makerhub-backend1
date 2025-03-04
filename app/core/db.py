import mongoengine
import os
from minio import Minio
from minio.error import S3Error
from fastapi import HTTPException
from app.core.config import settings
from loguru import logger

def connect_to_mongodb():
    """连接到MongoDB"""
    try:
        logger.info("正在连接到MongoDB...")
        # 修改连接方式，使用环境变量中的配置
        mongoengine.connect(host=os.getenv("MONGODB_URI"))
        logger.info("MongoDB连接成功")
    except Exception as e:
        logger.error(f"连接MongoDB失败: {e}")
        raise e

def disconnect_from_mongodb():
    """断开MongoDB连接"""
    try:
        logger.info("正在关闭MongoDB连接...")
        mongoengine.disconnect()
        logger.info("MongoDB连接已关闭")
    except Exception as e:
        logger.error(f"关闭MongoDB连接失败: {e}")

# MinIO client
class MinioClient:
    def __init__(self):
        try:
            logger.info(f"Connecting to MinIO at {settings.MINIO_ENDPOINT}")
            logger.info(f"Secure: {settings.MINIO_SECURE}")
            self.client = Minio(
                settings.MINIO_ENDPOINT,
                access_key=settings.MINIO_ACCESS_KEY,
                secret_key=settings.MINIO_SECRET_KEY,
                secure=settings.MINIO_SECURE,
                http_client=None  # 添加这行
            )
            self._ensure_bucket_exists()
        except Exception as e:
            logger.error(f"MinIO connection failed: {e}")
            raise e

    def _ensure_bucket_exists(self):
        try:
            logger.info(f"Checking if bucket '{settings.MINIO_BUCKET}' exists")
            if not self.client.bucket_exists(settings.MINIO_BUCKET):
                logger.info(f"Creating bucket '{settings.MINIO_BUCKET}'")
                self.client.make_bucket(settings.MINIO_BUCKET)
                logger.info(f"Bucket '{settings.MINIO_BUCKET}' created successfully")
            else:
                logger.info(f"Bucket '{settings.MINIO_BUCKET}' already exists")
        except Exception as e:
            logger.error(f"Bucket operation failed: {e}")
            raise e

    def get_file(self, filename: str) -> tuple[bytes, str]:
        try:
            data = self.client.get_object(settings.MINIO_BUCKET, filename)
            return data.read(), data.info().get("Content-Type", "application/octet-stream")
        except S3Error as e:
            raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

# Initialize clients
minio_client = MinioClient()
