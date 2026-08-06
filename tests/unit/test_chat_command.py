from dataclasses import FrozenInstanceError

import pytest

from app.application.commands.chat_command import ChatCommand


def test_chat_command_creation() -> None:
    command = ChatCommand(
        prompt="Hello",
        model="llama-3.3-70b-versatile",
        provider="groq",
    )

    assert command.prompt == "Hello"
    assert command.model == "llama-3.3-70b-versatile"
    assert command.provider == "groq"


def test_chat_command_is_immutable() -> None:
    command = ChatCommand(
        prompt="Hello",
        model="llama-3.3-70b-versatile",
        provider="groq",
    )

    with pytest.raises(FrozenInstanceError):
        command.prompt = "Changed"  # type: ignore[misc]
