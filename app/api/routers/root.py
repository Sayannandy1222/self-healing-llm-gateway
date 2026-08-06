from fastapi import APIRouter

from app.core.settings import settings

router = APIRouter(tags=["Root"])


@router.get("/", summary="Service Status")
async def root():
    """
    Service status endpoint.
    """

    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_environment,
        "status": "running",
    }