from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
async def root() -> JSONResponse:
    return JSONResponse(
        {
            "service": "Self-Healing LLM Gateway",
            "version": "0.1.0",
            "environment": "development",
            "status": "running",
        }
    )
