from __future__ import annotations

import pytest

from app.application.provider_selection.cost.provider_costs import (
    ProviderCosts,
)


def test_register_cost() -> None:
    costs = ProviderCosts()

    costs.register(
        "groq",
        0.20,
    )

    assert costs.get("groq") == 0.20


def test_default_cost() -> None:
    costs = ProviderCosts()

    assert costs.get("gemini") == 1.0


def test_lower_cost_has_higher_score() -> None:
    costs = ProviderCosts()

    costs.register(
        "groq",
        0.2,
    )

    costs.register(
        "gemini",
        0.5,
    )

    assert costs.score("groq") > costs.score("gemini")


def test_negative_cost() -> None:
    costs = ProviderCosts()

    with pytest.raises(ValueError):
        costs.register(
            "groq",
            -1,
        )
