from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager


class Tracer:
    """
    Lightweight tracing abstraction.

    This class can later be backed by OpenTelemetry without
    changing the rest of the application.
    """

    @contextmanager
    def start_span(
        self,
        name: str,
    ) -> Iterator[None]:
        """
        Start a tracing span.
        """

        _ = name

        try:
            yield
        finally:
            pass
