from __future__ import annotations

from app.application.commands.chat_command import ChatCommand
from app.application.pipeline.chat_pipeline import ChatPipeline
from app.domain.entities.chat_result import ChatResult


class ChatHandler:
    """
    Executes the Chat use case.
    """

    def __init__(
        self,
        pipeline: ChatPipeline,
    ) -> None:
        self._pipeline = pipeline

    async def execute(
        self,
        command: ChatCommand,
    ) -> ChatResult:
        """
        Execute a chat command.
        """

        return await self._pipeline.execute(command)
