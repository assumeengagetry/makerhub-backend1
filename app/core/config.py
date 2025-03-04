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
    MONGODB_URI: str = os.getenv("MONGODB_URI")

    
    # MinIO
    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", "minio:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_SECRET_KEY", "minioadmin")
    MINIO_PUBLIC_URL: str = os.getenv("MINIO_PUBLIC_URL", "http://minio:9000")
    MINIO_BUCKET: str = os.getenv("MINIO_BUCKET", "makerhub-files")
    MINIO_SECURE: bool = os.getenv("MINIO_SECURE", "false").lower() == "true"  # 确保是布尔值

    # JWT
    SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

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
    WECHAT_APPID = "wx4f3a36d5ea82ed7d"
    WECHAT_SECRET = "24b2a16a5981149b0287334beed24e88"
    WECHAT_LOGIN_URL = "https://api.weixin.qq.com/sns/jscode2session"

    class Config:
        case_sensitive = True

settings = Settings()  # 实例化配置类