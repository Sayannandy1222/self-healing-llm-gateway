from __future__ import annotations

from app.application.provider_selection.fallback.fallback_chain import (
    FallbackChain,
)


def test_fallback_chain() -> None:
    chain = FallbackChain(
        primary="groq",
        fallback="gemini",
    )

    assert chain.primary == "groq"
    assert chain.fallback == "gemini"
