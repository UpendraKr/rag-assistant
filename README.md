# Overview of project

This is a project designed to explore rag pipeline including embeddings, vector database using fastapi framework

# Project setup
mkdir rag-assistant
cd rag-assistant

git clone

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

docker compose up --build
docker compose up -d
docker compose down

# Logs
docker compose logs api
docker compose logs postgres
docker compose logs redis
docker compose logs qdrant

# Check running containers
docker ps

# Verify services
1. Fast API          - http://localhost:8000
2. Qdrant dashbaord  - http://localhost:6333/dashboard
3. PostgreSQL and Redis don't have browser UIs by default


# Craete sql tables
alembic revision --autogenerate -m "create documents table"
alembic upgrade head

docker exec -it rag-postgres psql -U postgres -d rag_db

# Run data/scripts
python -m scripts.init_qdrant
python -m scripts.create_document
python -m scripts.index_document
python -m scripts.test_retriever
python -m scripts.test_context
python -m scripts.test_rag
python -m scripts.test_langchain_llm
python -m scripts.test_langchain_retriever
python -m scripts.test_langchain_rag

# services we have
PDFParser
    ↓
"Extract text"

ChunkingService
    ↓
"Split text"

EmbeddingService
    ↓
"Create vectors"

QdrantService
    ↓
"Store/search vectors"

Retriever
    ↓
"Find relevant chunks"

ContextBuilder
    ↓
"Prepare context"

LLMService
    ↓
"Generate answer"

RAGService
    ↓
"Orchestrate the entire process"

# Understanding Qdrant Internals
1. tables ---> collections
2. rows   ---> Point
               
               Point
                ├── ID           
                ├── Vector    (Embedding)
                └── Payload   (meta_data)

                example :
                  chunk text - FastAPI supports async programming.
                  Embedding - [0.24, -0.81, 0.13, ...]
                  meta_data - { "document": "fastapi.pdf", "page": 12, "section": "Async", "version": "1.0" }  

                  Record in Qdrant:
                     ID: 101

                     Vector:
                     [0.24, -0.81, ...]

                     Payload:
                     {
                      document: fastapi.pdf,
                      page:12,
                      section:Async
                     } 

   Collection

      │

      ├── Point

      │      ├── Vector

      │      ├── Payload

      │      └── ID

      │

      ├── Point

      ├── Point

      └── Point

4. Distance Metrics:    How does Qdrant know two vectors are similar?
   1. Cosine Similarity            (small angle  , high Similarity)
   2. Dot Product
   3. Euclidean Distance