from __future__ import annotations

from typing import Protocol

from app.application.commands.chat_command import ChatCommand
from app.domain.entities.chat_result import ChatResult
from app.domain.providers.provider import LLMProvider
from app.infrastructure.cache.cache import Cache


class ProviderSelectorProtocol(Protocol):
    """
    Contract implemented by provider selectors.
    """

    def select(self) -> LLMProvider: ...


class ChatPipeline:
    """
    Production request execution pipeline with automatic provider failover
    and response caching.
    """

    def __init__(
        self,
        provider_selector: ProviderSelectorProtocol,
        cache: Cache | None = None,
    ) -> None:
        self._provider_selector = provider_selector
        self._cache = cache

    async def execute(
        self,
        command: ChatCommand,
    ) -> ChatResult:
        """
        Execute a chat request.

        Cached responses are returned immediately. If the selected
        provider fails, automatically retry with the next provider.
        """

        cache_key = command.prompt

        if self._cache is not None:
            cached = self._cache.get(cache_key)

            if cached is not None:
                return ChatResult(
                    response=cached,
                    provider="cache",
                    model="in-memory",
                )

        provider = self._provider_selector.select()

        try:
            result = await provider.chat(
                prompt=command.prompt,
            )

            if self._cache is not None:
                self._cache.set(
                    key=cache_key,
                    value=result.response,
                    ttl=300,
                )

            return result

        except Exception:
            fallback = self._provider_selector.select()

            result = await fallback.chat(
                prompt=command.prompt,
            )

            if self._cache is not None:
                self._cache.set(
                    key=cache_key,
                    value=result.response,
                    ttl=300,
                )

            return result
