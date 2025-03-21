from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from loguru import logger
from app.core.db import connect_to_mongodb, disconnect_from_mongodb
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.auth import AuthMiddleware
from app.routes import (
    u1ser_router,
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
    connect_to_mongodb()
    logger.info("应用启动 - 已连接到MongoDB")

@app.on_event("shutdown")
async def shutdown_event():
    disconnect_from_mongodb()
    logger.info("应用关闭 - 已断开MongoDB连接")

# API路由注册
PREFIX = "/api"

# 用户和认证
app.include_router(u1ser_router.router, prefix=f"{PREFIX}/users", tags=["用户管理"])

# # 工作管理
# app.include_router(s14chedule_router.router, prefix=f"{PREFIX}/schedules", tags=["排班管理"])
# app.include_router(d12uty_router.router, prefix=f"{PREFIX}/duties", tags=["值班管理"])
# app.include_router(d11uty_apply_router.router, prefix=f"{PREFIX}/duty_apply", tags=["值班申請管理"])
# app.include_router(c13leaning_router.router, prefix=f"{PREFIX}/cleaning", tags=["清洁管理"])
# app.include_router(t5ask_router.router, prefix=f"{PREFIX}/tasks", tags=["任务管理"])

# # 资源管理
# app.include_router(s7tuff_router.router, prefix=f"{PREFIX}/stuff", tags=["物品管理"])
# app.include_router(b6orrow_stuff_router.router, prefix=f"{PREFIX}/borrow_stuff", tags=["借用物品管理"])
# app.include_router(v8enue_router.router, prefix=f"{PREFIX}/venues", tags=["场地管理"])
# # app.include_router(p3rinter_router.router, prefix=f"{PREFIX}/printers", tags=["打印管理"])
# app.include_router(r17esource_router.router, prefix=f"{PREFIX}/resources", tags=["MinIO资源"])

# # # 活动管理
# app.include_router(e4vent_router.router, prefix=f"{PREFIX}/events", tags=["活动管理"])
# # app.include_router(c10ompetition_router.router, prefix=f"{PREFIX}/competitions", tags=["比赛管理"])
# # app.include_router(p9roject_router.router, prefix=f"{PREFIX}/projects", tags=["项目管理"])

# # 通信和文档
# app.include_router(m15essage_router.router, prefix=f"{PREFIX}/messages", tags=["消息管理"])
# app.include_router(x16iumi_router.router, prefix=f"{PREFIX}/xiumi", tags=["秀米管理"])
# app.include_router(r2egulation_router.router, prefix=f"{PREFIX}/regulations", tags=["规章制度"])

# 健康检查
@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": app.version}

@app.get("/")
async def root():
    return {"message": "fuck you !"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=settings.WORKERS
    )