from __future__ import annotations

import traceback
from collections.abc import MutableMapping
from typing import Any

EventDict = MutableMapping[str, Any]


def add_exception_details(
    logger: object,
    method_name: str,
    event_dict: EventDict,
) -> EventDict:
    """
    Enrich log events with structured exception details.
    """

    del logger
    del method_name

    exc = event_dict.pop("exception", None)

    if exc is None:
        return event_dict

    event_dict["exception_type"] = type(exc).__name__
    event_dict["exception_message"] = str(exc)

    event_dict["stacktrace"] = traceback.format_exception(
        type(exc),
        exc,
        exc.__traceback__,
    )

    return event_dict
