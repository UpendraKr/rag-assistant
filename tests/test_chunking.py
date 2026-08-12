from app.services.chunking import ChunkingService


text = """
FastAPI is a modern Python web framework.

It can be used to build APIs.

FastAPI supports dependency injection.

It also supports OAuth2 authentication.

JWT tokens are commonly used for authentication.
"""

service = ChunkingService(
    chunk_size=100,
    chunk_overlap=20,
)

chunks = service.split(text)

for index, chunk in enumerate(chunks):
    print(f"\n--- Chunk {index} ---")
    print(chunk)