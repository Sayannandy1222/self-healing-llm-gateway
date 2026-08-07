from __future__ import annotations

from app.application.commands.chat_command import ChatCommand
from app.application.resolver.provider_selector import ProviderSelector
from app.domain.entities.chat_result import ChatResult


class ChatPipeline:
    """
    Production request execution pipeline.
    """

    def __init__(
        self,
        provider_selector: ProviderSelector,
    ) -> None:
        self._provider_selector = provider_selector

    async def execute(
        self,
        command: ChatCommand,
    ) -> ChatResult:
        """
        Execute a chat command.
        """

        provider = self._provider_selector.select()

        return await provider.chat(
            prompt=command.prompt,
        )
