from __future__ import annotations

from contextvars import ContextVar
from uuid import uuid4

_request_id: ContextVar[str | None] = ContextVar(
    "request_id",
    default=None,
)

_correlation_id: ContextVar[str | None] = ContextVar(
    "correlation_id",
    default=None,
)


def generate_request_id() -> str:
    """
    Generate a unique request identifier.
    """
    return uuid4().hex


def generate_correlation_id() -> str:
    """
    Generate a unique correlation identifier.
    """
    return uuid4().hex


def set_request_id(request_id: str) -> None:
    """
    Store the current request ID.
    """
    _request_id.set(request_id)


def get_request_id() -> str | None:
    """
    Return the current request ID.
    """
    return _request_id.get()


def set_correlation_id(correlation_id: str) -> None:
    """
    Store the current correlation ID.
    """
    _correlation_id.set(correlation_id)


def get_correlation_id() -> str | None:
    """
    Return the current correlation ID.
    """
    return _correlation_id.get()


def clear_context() -> None:
    """
    Clear request-scoped context.
    """
    _request_id.set(None)
    _correlation_id.set(None)
