from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_router
from app.core.cors.cors_config import CORSConfig
from app.core.lifespan import lifespan

app = FastAPI(
    title="Self-Healing LLM Gateway",
    version="1.0.0",
    lifespan=lifespan,
)

cors = CORSConfig()

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors.allow_origins,
    allow_methods=cors.allow_methods,
    allow_headers=cors.allow_headers,
    allow_credentials=cors.allow_credentials,
)

app.include_router(api_router)
