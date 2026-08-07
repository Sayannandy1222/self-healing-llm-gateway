from __future__ import annotations

from fastapi import APIRouter

from app.api.routers.chat import router as chat_router
from app.api.routers.health import router as health_router
from app.api.routers.metrics import router as metrics_router
from app.api.routers.root import router as root_router

api_router = APIRouter()

api_router.include_router(root_router)
api_router.include_router(health_router)
api_router.include_router(chat_router)
api_router.include_router(metrics_router)
