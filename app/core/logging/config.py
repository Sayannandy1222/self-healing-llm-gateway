from __future__ import annotations

import logging
import sys

import structlog

from app.core.logging.filters import mask_sensitive_fields
from app.core.logging.processors import (
    add_application_metadata,
    add_request_metadata,
)


def configure_logging() -> None:
    """
    Configure the application's structured logging pipeline.
    """

    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(message)s",
    )

    structlog.configure(
        processors=[
            add_application_metadata,
            add_request_metadata,
            mask_sensitive_fields,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            logging.INFO,
        ),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )
