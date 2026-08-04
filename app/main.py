from fastapi import FastAPI, APIRouter
from app.api.health import router as health_router

app = FastAPI(
    title="RAG Assistant",
    version="1.0.0"
)

app.include_router(health_router)

@app.get("/")
def home():
    return {
        "status": "running"
    }