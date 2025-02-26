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
# 这地方还有一堆索引没写，我先写一个示例，后面的再说
class MongoDB:
    def connect_to_database(self):
        try:
            logger.info("正在连接到MongoDB...")
            # 使用connect()函数连接到MongoDB
            self.connection = connect(
                db=settings.MONGO_DB,
                host=settings.MONGO_URI
            )
            self.db = self.connection.get_database(settings.MONGO_DB)
            logger.info("MongoDB连接成功")
            
            # 确保必要的集合存在并创建索引
            self._ensure_collections()
            self.create_indexes()
            
        except Exception as e:
            logger.error(f"连接MongoDB失败: {e}")
            raise e

    def _ensure_collections(self):
        """确保所有必要的集合存在"""
        required_collections = ['users', 'duty_records', 'borrow_records']
        existing_collections = self.db.list_collection_names()
        
        for collection in required_collections:
            if collection not in existing_collections:
                logger.info(f"创建集合: {collection}")
                self.db.create_collection(collection)

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
           
            # 为users集合创建索引
            self.db.users.create_index("userid", unique=True)
            logger.info("users集合索引创建成功")
            
            # 为duty_records集合创建索引
            self.db.duty_records.create_index("userid")
            logger.info("duty_records集合索引创建成功")
            
            # 为borrow_records集合创建索引
            self.db.borrow_records.create_index("apply_id", unique=True)
            logger.info("borrow_records集合索引创建成功")
            
            logger.info("所有MongoDB索引创建完成")
        except Exception as e:
            logger.error(f"创建MongoDB索引失败: {e}")
            raise e

    def get_db(self) -> Generator:
        try:
            yield me.connection.get_db()  # 通过 MongoEngine 获取数据库
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
