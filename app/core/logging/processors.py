from __future__ import annotations

import logging
from collections.abc import MutableMapping
from typing import Any

from app.core.context.request_context import (
    get_correlation_id,
    get_request_id,
)
from app.core.settings import settings

EventDict = MutableMapping[str, Any]


def add_application_metadata(
    logger: logging.Logger,
    method_name: str,
    event_dict: EventDict,
) -> EventDict:
    """
    Inject application metadata into every log record.
    """

    del logger
    del method_name

    event_dict["service"] = settings.app_name
    event_dict["environment"] = settings.environment
    event_dict["version"] = settings.app_version

    return event_dict


def add_request_metadata(
    logger: logging.Logger,
    method_name: str,
    event_dict: EventDict,
) -> EventDict:
    """
    Inject request-scoped metadata.
    """

    del logger
    del method_name

    event_dict["request_id"] = get_request_id()
    event_dict["correlation_id"] = get_correlation_id()

    return event_dict
