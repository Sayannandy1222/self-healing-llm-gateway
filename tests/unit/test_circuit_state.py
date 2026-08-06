from app.core.resilience.circuit_state import CircuitState


def test_circuit_states() -> None:
    """
    Verify all supported circuit states.
    """

    assert CircuitState.CLOSED.value == "closed"

    assert CircuitState.OPEN.value == "open"

    assert CircuitState.HALF_OPEN.value == "half_open"
