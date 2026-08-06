from app.core.resilience.retry_policy import RetryPolicy


def test_retry_policy_defaults() -> None:
    policy = RetryPolicy()

    assert policy.max_attempts == 3
    assert policy.initial_delay == 0.5
    assert policy.backoff_factor == 2.0
    assert policy.max_delay == 8.0
    assert policy.jitter is True
