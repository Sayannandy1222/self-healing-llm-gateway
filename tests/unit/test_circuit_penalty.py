from __future__ import annotations

from app.application.provider_selection.circuit_penalty.circuit_penalty import (
    CircuitPenalty,
    CircuitState,
)


def test_closed_circuit_score() -> None:
    assert (
        CircuitPenalty.score(
            CircuitState.CLOSED,
        )
        == 100.0
    )


def test_half_open_circuit_score() -> None:
    assert (
        CircuitPenalty.score(
            CircuitState.HALF_OPEN,
        )
        == 70.0
    )


def test_open_circuit_score() -> None:
    assert (
        CircuitPenalty.score(
            CircuitState.OPEN,
        )
        == 20.0
    )
