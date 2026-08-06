from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/health")
async def health() -> JSONResponse:
    return JSONResponse(
        {
            "status": "healthy",
            "service": "Self-Healing LLM Gateway",
            "version": "0.1.0",
        }
    )


@router.get("/ready")
async def readiness() -> JSONResponse:
    return JSONResponse(
        {
            "status": "ready",
        }
    )


@router.get("/live")
async def liveness() -> JSONResponse:
    return JSONResponse(
        {
            "status": "alive",
        }
    )
