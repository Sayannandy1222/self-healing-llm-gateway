from __future__ import annotations

from collections.abc import Awaitable, Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.context.request_context import (
    clear_context,
    generate_correlation_id,
    generate_request_id,
    set_correlation_id,
    set_request_id,
)


class RequestContextMiddleware(BaseHTTPMiddleware):
    """
    Middleware responsible for creating and propagating
    request-scoped context.
    """

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:

        request_id = request.headers.get(
            "X-Request-ID",
            generate_request_id(),
        )

        correlation_id = request.headers.get(
            "X-Correlation-ID",
            generate_correlation_id(),
        )

        set_request_id(request_id)
        set_correlation_id(correlation_id)

        try:
            response = await call_next(request)

            response.headers["X-Request-ID"] = request_id
            response.headers["X-Correlation-ID"] = correlation_id

            return response

        finally:
            clear_context()
