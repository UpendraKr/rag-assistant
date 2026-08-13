from fastapi import APIRouter

from app.schemas.rag import (
    RAGQueryRequest,
    RAGQueryResponse,
)

from app.services.context_builder import (
    ContextBuilder,
)

from app.services.embeddings import (
    get_embedding_service,
)

from app.services.llm import LLMService

from app.services.qdrant_service import (
    QdrantService,
)

from app.services.rag_service import (
    RAGService,
)

from app.services.retriever import (
    Retriever,
)


router = APIRouter(
    prefix="/api/v1/rag",
    tags=["RAG"],
)


def get_rag_service():

    retriever = Retriever(
        embedding_service=(
            get_embedding_service()
        ),
        qdrant_service=QdrantService(),
    )

    return RAGService(
        retriever=retriever,
        context_builder=ContextBuilder(),
        llm_service=LLMService(),
    )


@router.post(
    "/query",
    response_model=RAGQueryResponse,
)
def query_rag(
    request: RAGQueryRequest,
):
    service = get_rag_service()
    return service.answer(
        question=request.question,
        document_id=request.document_id,
        score_threshold=request.score_threshold,
    )