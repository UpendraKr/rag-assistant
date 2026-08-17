from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

from app.core.config import settings
from app.db.qdrant import client


embeddings = OpenAIEmbeddings(
    model=settings.EMBEDDING_MODEL,
    api_key=settings.OPENAI_API_KEY,
)


vector_store = QdrantVectorStore(
    client=client,
    collection_name=settings.QDRANT_COLLECTION,
    embedding=embeddings,
)

retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 5,
    }
)

# documents = retriever.invoke(
#     "What is this document about?"
# )