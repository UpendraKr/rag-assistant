from fastapi import FastAPI, APIRouter
from app.api.v1.health import router as health_router
from app.api.v1.rag import router as rag_router

app = FastAPI(
    title="RAG Assistant",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(rag_router)

@app.get("/")
def home():
    return {
        "status": "running"
    }