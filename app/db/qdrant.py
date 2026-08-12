from qdrant_client import QdrantClient
from app.core.config import settings
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(
    url=settings.QDRANT_URL
)

def create_collection():

    collections = client.get_collections()

    existing = {
        collection.name
        for collection in collections.collections
    }

    if settings.QDRANT_COLLECTION not in existing:

        client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,
            vectors_config=VectorParams(
                size=settings.VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )