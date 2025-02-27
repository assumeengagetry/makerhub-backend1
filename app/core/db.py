import mongoengine as me
from minio import Minio
from minio.error import S3Error
from mongoengine import connect, Document, StringField, IntField, BinaryField
from fastapi import HTTPException, Depends, status
from app.core.config import settings
from loguru import logger
import io
from typing import Generator

class MongoDB:
    def __init__(self):
        self.connection = None
        self.db = None

    def connect_to_database(self):
        try:
            logger.info("正在连接到MongoDB...")
            self.connection = connect(
                db=settings.MONGO_DB,
                host=settings.MONGO_URI
            )
            self.db = self.connection[settings.MONGO_DB]
            logger.info("MongoDB连接成功")
            
            # 确保必要的集合存在并创建索引
            self._ensure_collections()
            self.create_indexes()
            
        except Exception as e:
            logger.error(f"连接MongoDB失败: {e}")
            raise e
        
    def close_database_connection(self):
        try:
            logger.info("正在关闭MongoDB连接...")
            me.disconnect()  # 使用 MongoEngine 的 disconnect 来关闭连接
            logger.info("MongoDB连接已关闭")
        except Exception as e:
            logger.error(f"关闭MongoDB连接失败: {e}")

    def get_db(self) -> Generator:
        try:
            yield me.connection.get_db()  # 通过 MongoEngine 获取数据库
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    def get_database(self):
        if not self.db:
            self.connect_to_database()
        return self.db

    def get_collection(self, collection_name: str):
        return self.get_database()[collection_name]

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
mongodb = MongoDB()
minio_client = MinioClient()
