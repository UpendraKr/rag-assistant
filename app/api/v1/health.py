from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(
    prefix="/api/v1/health",
)


@router.get("/")
def health():
    return {
        "environment": settings.ENV,
        "debug": settings.DEBUG
    }