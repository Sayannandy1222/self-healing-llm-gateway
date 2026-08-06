import asyncio

import pytest

from app.core.resilience.timeout_executor import TimeoutExecutor
from app.core.resilience.timeout_policy import TimeoutPolicy


@pytest.mark.asyncio
async def test_timeout_executor_returns_result() -> None:
    executor = TimeoutExecutor(
        TimeoutPolicy(timeout_seconds=1.0),
    )

    async def operation() -> str:
        return "success"

    result = await executor.execute(operation)

    assert result == "success"


@pytest.mark.asyncio
async def test_timeout_executor_times_out() -> None:
    executor = TimeoutExecutor(
        TimeoutPolicy(timeout_seconds=0.01),
    )

    async def operation() -> str:
        await asyncio.sleep(0.1)
        return "late"

    with pytest.raises(asyncio.TimeoutError):
        await executor.execute(operation)
