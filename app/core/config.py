import pydantic
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()  # 加载环境变量

class Settings(pydantic.ConfigDict):
    # 项目设置
    PROJECT_NAME: str = "MakerHub"
    API_V1_STR: str = "/api"
    
    # MongoDB
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB: str = os.getenv("MONGO_DB", "makerhub_db")

    # MinIO
    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", "localhost:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_SECRET_KEY", "minioadmin")
    MINIO_BUCKET: str = os.getenv("MINIO_BUCKET", "makerhub-files")
    MINIO_SECURE: bool = os.getenv("MINIO_SECURE", "False").lower() == "true"
    MINIO_BUCKET_NAME: str = os.getenv("MINIO_BUCKET_NAME", "public-resources")
    MINIO_PUBLIC_URL: str = os.getenv("MINIO_PUBLIC_URL", "http://localhost:9000")

    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "_assume060801Xsk_")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "2880"))

    # 权限等级定义
    PERMISSION_LEVELS = {
        "USER": 0,      # 普通用户
        "ADMIN": 1,     # 管理员
        "SUPER": 2      # 超级管理员
    }

    # 应用设置
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    WORKERS: int = int(os.getenv("WORKERS", "4"))

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]

    # 微信小程序配置
    WECHAT_APPID = "your-appid"
    WECHAT_SECRET = "your-secret"
    WECHAT_LOGIN_URL = "https://api.weixin.qq.com/sns/jscode2session"

    class Config:
        case_sensitive = True

settings = Settings()  # 实例化配置类