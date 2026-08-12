from app.services.embeddings.base import EmbeddingProvider


class EmbeddingService:

    def __init__(
        self,
        provider: EmbeddingProvider,
    ):
        self.provider = provider

    def embed_text(
        self,
        text: str,
    ) -> list[float]:

        text = text.strip()

        if not text:
            raise ValueError(
                "Text cannot be empty"
            )

        return self.provider.embed_text(text)

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        cleaned_texts = [
            text.strip()
            for text in texts
            if text.strip()
        ]

        if not cleaned_texts:
            raise ValueError(
                "No valid texts provided"
            )

        return self.provider.embed_documents(
            cleaned_texts
        )