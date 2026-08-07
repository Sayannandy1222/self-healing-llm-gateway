from __future__ import annotations

from app.application.provider_selection.sticky.sticky_provider_registry import (
    StickyProviderRegistry,
)


def test_assign_provider() -> None:
    registry = StickyProviderRegistry()

    registry.assign(
        "session-1",
        "groq",
    )

    assert registry.get("session-1") == "groq"


def test_contains_assignment() -> None:
    registry = StickyProviderRegistry()

    registry.assign(
        "session-1",
        "groq",
    )

    assert registry.contains("session-1")


def test_remove_assignment() -> None:
    registry = StickyProviderRegistry()

    registry.assign(
        "session-1",
        "groq",
    )

    registry.remove("session-1")

    assert registry.get("session-1") is None


def test_clear_assignments() -> None:
    registry = StickyProviderRegistry()

    registry.assign("a", "groq")
    registry.assign("b", "gemini")

    registry.clear()

    assert registry.sessions() == []


def test_sessions() -> None:
    registry = StickyProviderRegistry()

    registry.assign("b", "gemini")
    registry.assign("a", "groq")

    assert registry.sessions() == [
        "a",
        "b",
    ]
