from __future__ import annotations

from typing import Protocol

from app.application.commands.chat_command import ChatCommand
from app.domain.entities.chat_result import ChatResult
from app.domain.providers.provider import LLMProvider


class ProviderSelectorProtocol(Protocol):
    """
    Contract implemented by provider selectors.
    """

    def select(self) -> LLMProvider: ...


class ChatPipeline:
    """
    Production request execution pipeline with automatic provider failover.
    """

    def __init__(
        self,
        provider_selector: ProviderSelectorProtocol,
    ) -> None:
        self._provider_selector = provider_selector

    async def execute(
        self,
        command: ChatCommand,
    ) -> ChatResult:
        """
        Execute a chat request.

        If the selected provider fails, automatically retry with the
        next provider returned by the selector.
        """

        provider = self._provider_selector.select()

        try:
            return await provider.chat(
                prompt=command.prompt,
            )

        except Exception:
            fallback = self._provider_selector.select()

            return await fallback.chat(
                prompt=command.prompt,
            )
