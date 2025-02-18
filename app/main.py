from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from loguru import logger

from app.core.config import settings
from app.core.logging import setup_logging
from app.core.auth import AuthMiddleware
from app.core.db import mongo
from app.routes import (
    user_router,
    schedule_router, 
    borrow_router,
    item_router, 
    duty_router,
    message_router,
    xiumi_router,
    cleaning_router,
    competition_router,
    venue_router,
    task_router,
    printer_router,
    project_router,
    event_router,
    regulation_router
)

# 初始化应用
app = FastAPI(
    title="MakerHub API",
    description="MakerHub后端API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 认证中间件
app.middleware("http")(AuthMiddleware())

# 全局异常处理
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body}
    )

# 数据库连接管理
@app.on_event("startup")
async def startup_event():
    setup_logging()
    await mongo.connect_to_database()
    logger.info("应用启动 - 已连接到MongoDB")

@app.on_event("shutdown")
async def shutdown_event():
    await mongo.close_database_connection()
    logger.info("应用关闭 - 已断开MongoDB连接")

# API路由注册
PREFIX = "/api/v1"

# 用户和认证
app.include_router(user_router.router, prefix=f"{PREFIX}/users", tags=["用户管理"])

# 工作管理
app.include_router(schedule_router.router, prefix=f"{PREFIX}/schedules", tags=["排班管理"])
app.include_router(duty_router.router, prefix=f"{PREFIX}/duties", tags=["值班管理"])
app.include_router(cleaning_router.router, prefix=f"{PREFIX}/cleaning", tags=["清洁管理"])
app.include_router(task_router.router, prefix=f"{PREFIX}/tasks", tags=["任务管理"])

# 资源管理
app.include_router(item_router.router, prefix=f"{PREFIX}/items", tags=["物品管理"])
app.include_router(borrow_router.router, prefix=f"{PREFIX}/borrows", tags=["借用管理"])
app.include_router(venue_router.router, prefix=f"{PREFIX}/venues", tags=["场地管理"])
app.include_router(printer_router.router, prefix=f"{PREFIX}/printers", tags=["打印管理"])

# 活动管理
app.include_router(event_router.router, prefix=f"{PREFIX}/events", tags=["活动管理"])
app.include_router(competition_router.router, prefix=f"{PREFIX}/competitions", tags=["比赛管理"])
app.include_router(project_router.router, prefix=f"{PREFIX}/projects", tags=["项目管理"])

# 通信和文档
app.include_router(message_router.router, prefix=f"{PREFIX}/messages", tags=["消息管理"])
app.include_router(xiumi_router.router, prefix=f"{PREFIX}/xiumi", tags=["秀米管理"])
app.include_router(regulation_router.router, prefix=f"{PREFIX}/regulations", tags=["规章制度"])

# 健康检查
@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": app.version}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=settings.WORKERS
    )