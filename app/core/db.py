from mongoengine import connect, disconnect
from minio import Minio
from minio.error import S3Error
from fastapi import HTTPException
from app.core.config import settings
from loguru import logger

def connect_to_mongodb():
    """连接到MongoDB"""
    try:
        logger.info("正在连接到MongoDB...")
        connect(
            db=settings.MONGODB_DATABASE,
            host=settings.MONGODB_URL,
            username=settings.MONGODB_USERNAME,
            password=settings.MONGODB_PASSWORD,
            authentication_source='admin'
        )
        logger.info("MongoDB连接成功")
    except Exception as e:
        logger.error(f"连接MongoDB失败: {e}")
        raise e

def disconnect_from_mongodb():
    """断开MongoDB连接"""
    try:
        logger.info("正在关闭MongoDB连接...")
        disconnect()
        logger.info("MongoDB连接已关闭")
    except Exception as e:
        logger.error(f"关闭MongoDB连接失败: {e}")
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
        # 检查桶是否存在，不存在则创建
        if not self.client.bucket_exists(settings.MINIO_BUCKET):
            self.client.make_bucket(settings.MINIO_BUCKET)
            logger.info(f"Bucket '{settings.MINIO_BUCKET}' 创建成功")
        else:
            logger.info(f"Bucket '{settings.MINIO_BUCKET}' 已存在")
        

    
    def get_file(self, filename: str) -> tuple[bytes, str]:
        try:
            data = self.client.get_object(settings.MINIO_BUCKET, filename)
            return data.read(), data.info().get("Content-Type", "application/octet-stream")
        except S3Error as e:
            raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

# Initialize clients
minio_client = MinioClient()
