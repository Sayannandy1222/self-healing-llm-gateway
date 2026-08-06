from app.core.resilience.circuit_breaker import CircuitBreaker
from app.core.resilience.circuit_state import CircuitState


def test_circuit_breaker_initial_state() -> None:
    breaker = CircuitBreaker()

    assert breaker.state is CircuitState.CLOSED
    assert breaker.failure_count == 0
    assert breaker.success_count == 0


def test_circuit_breaker_opens_after_threshold() -> None:
    breaker = CircuitBreaker(failure_threshold=3)

    breaker.record_failure()
    breaker.record_failure()

    assert breaker.failure_count == 2

    breaker.record_failure()

    assert breaker.failure_count == 3
    assert breaker.state is CircuitState.OPEN


def test_circuit_breaker_success_resets_failures() -> None:
    breaker = CircuitBreaker()

    breaker.record_failure()
    breaker.record_failure()

    breaker.record_success()

    assert breaker.failure_count == 0
    assert breaker.success_count == 1
    assert breaker.state is CircuitState.CLOSED


def test_circuit_breaker_reset() -> None:
    breaker = CircuitBreaker(failure_threshold=2)

    breaker.record_failure()
    breaker.record_failure()

    assert breaker.failure_count == 2
    assert breaker.state is CircuitState.OPEN

    breaker.reset()

    assert breaker.failure_count == 0
    assert breaker.success_count == 0
    assert breaker.state is CircuitState.CLOSED
