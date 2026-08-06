from __future__ import annotations

from app.application.commands.chat_command import ChatCommand
from app.application.resolver.provider_resolver import ProviderResolver
from app.domain.entities.chat_result import ChatResult


class ChatPipeline:
    """
    Production request execution pipeline.
    """

    def __init__(
        self,
        resolver: ProviderResolver,
    ) -> None:
        self._resolver = resolver

    async def execute(
        self,
        command: ChatCommand,
    ) -> ChatResult:
        """
        Execute a chat command.
        """

        provider = self._resolver.resolve("groq")

        return await provider.chat(
            prompt=command.prompt,
        )
