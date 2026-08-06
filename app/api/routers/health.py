from fastapi import APIRouter

from app.core.settings import settings

router = APIRouter(tags=["Health"])


@router.get("/health", summary="Health Check")
async def health():
    """
    Basic health endpoint.
    """

    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
    }


@router.get("/ready", summary="Readiness Check")
async def readiness():
    """
    Readiness endpoint.

    Later this will verify:
    - PostgreSQL
    - Redis
    - LLM Providers
    """

    return {
        "status": "ready",
    }


@router.get("/live", summary="Liveness Check")
async def liveness():
    """
    Liveness endpoint.
    """

    return {
        "status": "alive",
    }