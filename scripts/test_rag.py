from app.services.embeddings import get_embedding_service
from app.services.qdrant_service import QdrantService
from app.services.retriever import Retriever
from app.services.context_builder import ContextBuilder
from app.services.llm import LLMService
from app.services.rag_service import RAGService


retriever = Retriever(
    embedding_service=get_embedding_service(),
    qdrant_service=QdrantService(),
)

rag_service = RAGService(
    retriever=retriever,
    context_builder=ContextBuilder(),
    llm_service=LLMService(),
)


result = rag_service.answer(
    question="What is the ranking of IIT delhi as per NIRF in engineering 2021?",
    document_id=1,
)


print("\nANSWER:")
print(result["answer"])


print("\nSOURCES:")

for source in result["sources"]:

    print(source)