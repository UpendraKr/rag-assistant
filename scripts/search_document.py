from app.core.config import settings
from app.db.qdrant import client
from app.services.embeddings import get_embedding_service


embedding_service = get_embedding_service()


question = "What is this document about?"

query_vector = embedding_service.embed_text(
    question
)


results = client.query_points(
    collection_name=settings.QDRANT_COLLECTION,
    query=query_vector,
    limit=5,
).points


for result in results:

    print("\n" + "=" * 60)

    print("Score:", result.score)

    print(
        "Document:",
        result.payload["filename"],
    )

    print(
        "Page:",
        result.payload["page"],
    )

    print(
        "Chunk:",
        result.payload["chunk_index"],
    )

    print("\nText:")

    print(
        result.payload["text"]
    )