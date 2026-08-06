import pytest

from app.core.resilience.retry_executor import RetryExecutor


@pytest.mark.asyncio
async def test_retry_executor_returns_result() -> None:
    executor = RetryExecutor()

    async def operation() -> str:
        return "success"

    result = await executor.execute(operation)

    assert result == "success"


@pytest.mark.asyncio
async def test_retry_executor_retries_until_success() -> None:
    executor = RetryExecutor()

    attempts = 0

    async def operation() -> str:
        nonlocal attempts

        attempts += 1

        if attempts < 3:
            raise RuntimeError("temporary")

        return "ok"

    result = await executor.execute(operation)

    assert result == "ok"
    assert attempts == 3


@pytest.mark.asyncio
async def test_retry_executor_raises_after_max_attempts() -> None:
    executor = RetryExecutor()

    async def operation() -> str:
        raise RuntimeError("failure")

    with pytest.raises(RuntimeError):
        await executor.execute(operation)
