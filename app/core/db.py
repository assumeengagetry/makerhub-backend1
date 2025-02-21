import mongoengine as me
from minio import Minio
from minio.error import S3Error
from mongoengine import connect, Document, StringField, IntField, BinaryField
from fastapi import HTTPException, Depends, status
from app.core.config import settings
from loguru import logger
import io
from typing import Generator

# MongoDB client
class MongoDB:
    def connect_to_database(self):
        try:
            logger.info("正在连接到MongoDB...")
            me.connect(host=settings.MONGO_URI, db=settings.MONGO_DB)
            logger.info("MongoDB连接成功")
        except Exception as e:
            logger.error(f"连接MongoDB失败: {e}")

    def close_database_connection(self):
        try:
            logger.info("正在关闭MongoDB连接...")
            me.disconnect()  # 使用 MongoEngine 的 disconnect 来关闭连接
            logger.info("MongoDB连接已关闭")
        except Exception as e:
            logger.error(f"关闭MongoDB连接失败: {e}")

    def create_indexes(self):
        try:
            logger.info("正在创建MongoDB索引...")
            # 使用 MongoEngine 的同步方法创建索引
            me.connection.get_database().users.create_index("userid", unique=True)
            me.connection.get_database().duty_records.create_index("userid")
            me.connection.get_database().borrow_records.create_index("apply_id", unique=True)
            logger.info("MongoDB索引创建完成")
        except Exception as e:
            logger.error(f"创建MongoDB索引失败: {e}")

    def get_db(self) -> Generator:
        try:
            yield me.connection.get_database()  # 通过 MongoEngine 获取数据库
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    def get_collection(self, collection_name: str):
        # 同样的方式来获取集合
        # 不需要使用 Depends，直接调用 get_db 方法
        def get_collection_dependency():
            db = next(self.get_db())  # 获取数据库连接
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
mongo = MongoDB()
minio_client = MinioClient()
