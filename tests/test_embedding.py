from app.services.embeddings import get_embedding_service


service = get_embedding_service()

vector = service.embed_text(
    "FastAPI is a Python web framework."
)

print("Vector length:", len(vector))

print("First 5 values:", vector[:5])