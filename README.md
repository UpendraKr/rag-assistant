# Overview of project

This is a project designed to explore rag pipeline including embeddings, vector database using fastapi framework

# project setup
mkdir rag-assistant
cd rag-assistant

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

docker compose up --build
docker compose up -d
docker compose down

# logs
docker compose logs api
docker compose logs postgres
docker compose logs redis
docker compose logs qdrant

# check running containers
docker ps

# verify services
1. Fast API          - http://localhost:8000
2. Qdrant dashbaord  - http://localhost:6333/dashboard
3. PostgreSQL and Redis don't have browser UIs by default
