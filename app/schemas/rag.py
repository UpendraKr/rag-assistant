from pydantic import BaseModel, Field


class RAGQueryRequest(BaseModel):

    question: str = Field(
        min_length=1,
        max_length=2000,
    )
    document_id: int | None = None
    score_threshold: float | None = None


class RAGSource(BaseModel):
    document_id: int
    filename: str
    page: int
    score: float


class RAGQueryResponse(BaseModel):
    answer: str
    sources: list[RAGSource]