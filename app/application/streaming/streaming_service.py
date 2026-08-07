from __future__ import annotations

from collections.abc import AsyncIterator


class StreamingService:
    """
    Streams LLM responses token by token.
    """

    async def stream(
        self,
        response: str,
    ) -> AsyncIterator[str]:
        """
        Yield each token in the response.
        """

        for token in response.split():
            yield token + " "
