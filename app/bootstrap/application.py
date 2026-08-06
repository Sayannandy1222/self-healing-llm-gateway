from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_router
from app.core.exceptions import register_exception_handlers
from app.core.lifespan import lifespan
from app.core.logging import configure_logging
from app.core.settings import settings
from app.middleware.request_logging import RequestLoggingMiddleware


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    configure_logging()

    app = FastAPI(
        title=settings.app_name,
        description="Enterprise-grade Self-Healing LLM Gateway",
        version=settings.app_version,
        lifespan=lifespan,
    )

    register_exception_handlers(app)

    app.add_middleware(RequestLoggingMiddleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    return app