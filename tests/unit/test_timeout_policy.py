from app.core.resilience.timeout_policy import TimeoutPolicy


def test_timeout_policy_defaults() -> None:
    policy = TimeoutPolicy()

    assert policy.timeout_seconds == 30.0
