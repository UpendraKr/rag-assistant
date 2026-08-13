from app.services.embeddings import get_embedding_service
from app.services.qdrant_service import QdrantService
from app.services.retriever import Retriever
from app.services.context_builder import ContextBuilder


retriever = Retriever(
    embedding_service=get_embedding_service(),
    qdrant_service=QdrantService(),
)


results = retriever.search(
    query="IIT delhi ranking as per NIRF in engineering 2021?",
    limit=5,
    document_id=1,
)


builder = ContextBuilder()

context = builder.build(results)

print(context)