from app.services.embeddings.openai_provider import (
    OpenAIEmbeddingProvider,
)
from app.services.embeddings.service import EmbeddingService


def get_embedding_service() -> EmbeddingService:

    provider = OpenAIEmbeddingProvider()

    return EmbeddingService(
        provider=provider
    )