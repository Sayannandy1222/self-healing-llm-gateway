from __future__ import annotations

from collections.abc import MutableMapping
from typing import Any

EventDict = MutableMapping[str, Any]

SENSITIVE_KEYS = {
    "password",
    "token",
    "access_token",
    "refresh_token",
    "authorization",
    "api_key",
    "secret",
    "secret_key",
    "groq_api_key",
}

MASK = "********"


def _mask(value: object) -> object:
    """
    Recursively mask sensitive values in dictionaries and lists.
    """

    if isinstance(value, dict):
        masked: dict[str, object] = {}

        for key, item in value.items():
            if key.lower() in SENSITIVE_KEYS:
                masked[key] = MASK
            else:
                masked[key] = _mask(item)

        return masked

    if isinstance(value, list):
        return [_mask(item) for item in value]

    return value


def mask_sensitive_fields(
    logger: object,
    method_name: str,
    event_dict: EventDict,
) -> EventDict:
    """
    Structlog processor that masks sensitive values.
    """

    del logger
    del method_name

    for key, value in list(event_dict.items()):
        event_dict[key] = _mask(value)

        if key.lower() in SENSITIVE_KEYS:
            event_dict[key] = MASK

    return event_dict
