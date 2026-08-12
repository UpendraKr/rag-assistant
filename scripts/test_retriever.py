from app.services.embeddings import (
    get_embedding_service,
)

from app.services.qdrant_service import (
    QdrantService,
)

from app.services.retriever import Retriever


retriever = Retriever(
    embedding_service=get_embedding_service(),
    qdrant_service=QdrantService(),
)


results = retriever.search(
    query="What is this document about?",
    limit=5,
    document_id=1,
)


for result in results:

    print("\n" + "=" * 60)

    print("Score:", result.score)

    print("Page:", result.payload["page"])

    print("Text:")

    print(result.payload["text"])