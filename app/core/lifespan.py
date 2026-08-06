from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    Application lifespan events.
    """

    logger.info(
        {
            "event": "application.startup",
        }
    )

    yield

    logger.info(
        {
            "event": "application.shutdown",
        }
    )
