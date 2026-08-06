from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar

from app.core.resilience.timeout_policy import TimeoutPolicy

T = TypeVar("T")


class TimeoutExecutor:
    """
    Executes asynchronous operations with a timeout.
    """

    def __init__(
        self,
        policy: TimeoutPolicy,
    ) -> None:
        self._policy = policy

    async def execute(
        self,
        operation: Callable[[], Awaitable[T]],
    ) -> T:
        """
        Execute an operation while enforcing the timeout policy.
        """

        return await asyncio.wait_for(
            operation(),
            timeout=self._policy.timeout_seconds,
        )
