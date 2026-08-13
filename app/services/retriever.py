from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue,
)


class Retriever:

    def __init__(
        self,
        embedding_service,
        qdrant_service,
    ):
        self.embedding_service = embedding_service
        self.qdrant_service = qdrant_service

    def search(
        self,
        query: str,
        limit: int = 5,
        document_id: int | None = None,
        score_threshold: float | None = None,
    ):

        query_vector = (
            self.embedding_service
            .embed_text(query)
        )

        query_filter = None

        if document_id is not None:

            query_filter = Filter(
                must=[
                    FieldCondition(
                        key="document_id",
                        match=MatchValue(
                            value=document_id,
                        ),
                    )
                ]
            )

        return self.qdrant_service.search(
            vector=query_vector,
            limit=limit,
            query_filter=query_filter,
            score_threshold=score_threshold,
        )