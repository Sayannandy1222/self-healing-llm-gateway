from app.application.factories.provider_factory import ProviderFactory
from app.application.services.chat_service import ChatService


def get_chat_service() -> ChatService:
    """
    Dependency provider for ChatService.
    """

    provider = ProviderFactory.create()

    return ChatService(provider)
