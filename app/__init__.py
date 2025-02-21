from app.main import app
from app.core.config import settings
from fastapi.testclient import TestClient 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from loguru import logger
from app.core.logging import setup_logging
from app.core.auth import AuthMiddleware
from app.core.db import mongo
from app.routes import (
    u1ser_router,
    s14chedule_router, 
    b6orrow_stuff_router,
    s7tuff_router, 
    d12uty_router,
    d11uty_apply_router,
    m15essage_router,
    x16iumi_router,
    c13leaning_router,
    c10ompetition_router,
    v8enue_router,
    t5ask_router,
    p3rinter_router,
    p9roject_router,
    e4vent_router,
    r2egulation_router,
    r17esource_router,
)
