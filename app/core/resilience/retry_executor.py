from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar

from app.core.resilience.retry_policy import RetryPolicy

T = TypeVar("T")


class RetryExecutor:
    """
    Generic retry executor for transient failures.
    """

    def __init__(
        self,
        policy: RetryPolicy | None = None,
    ) -> None:
        self._policy = policy or RetryPolicy()

    async def execute(
        self,
        operation: Callable[[], Awaitable[T]],
    ) -> T:
        """
        Execute an asynchronous operation using exponential backoff.
        """

        delay = self._policy.initial_delay

        last_exception: Exception | None = None

        for attempt in range(self._policy.max_attempts):
            try:
                return await operation()

            except Exception as exc:
                last_exception = exc

                if attempt == self._policy.max_attempts - 1:
                    raise

                await asyncio.sleep(delay)

                delay = min(
                    delay * self._policy.backoff_factor,
                    self._policy.max_delay,
                )

        assert last_exception is not None

        raise last_exception
