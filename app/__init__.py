from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from loguru import logger
from mongoengine import connect, disconnect
from app.core.db import connect_to_mongodb, disconnect_from_mongodb
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.auth import AuthMiddleware
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