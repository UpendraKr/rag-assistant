from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(
    prefix="/api",
)


@router.get("/health")
def health():
    return {
        "environment": settings.ENV,
        "debug": settings.DEBUG
    }