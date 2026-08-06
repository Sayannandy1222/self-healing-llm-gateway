from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle management.
    """

    logger.info("application.startup")

    yield

    logger.info("application.shutdown")