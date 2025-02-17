from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.middleware.auth_middleware import AuthMiddleware
from app.utils.mongo_utils import mongo
from app.core.logging import setup_logging
from app.routes import (
    user_router, schedule_router, borrow_router, 
    item_router, duty_router, message_router
)

# 设置日志
logger = setup_logging()

app = FastAPI(
    title="社团管理系统API",
    description="社团管理系统后端API文档",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 添加认证中间件
app.middleware("http")(AuthMiddleware())

@app.on_event("startup")
async def startup_db_client():
    await mongo.connect_to_database()
    await mongo.create_indexes()
    logger.info("Connected to MongoDB")

@app.on_event("shutdown")
async def shutdown_db_client():
    await mongo.close_database_connection()
    logger.info("Disconnected from MongoDB")

# 注册路由
app.include_router(user_router.router, prefix="/api/users", tags=["用户管理"])
app.include_router(schedule_router.router, prefix="/api/schedules", tags=["排班管理"])
app.include_router(borrow_router.router, prefix="/api/borrows", tags=["借用管理"])
app.include_router(item_router.router, prefix="/api/items", tags=["物品管理"])
app.include_router(duty_router.router, prefix="/api/duties", tags=["值班管理"])
app.include_router(message_router.router, prefix="/api/messages", tags=["消息管理"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)