from app.prompts.rag import SYSTEM_PROMPT


class RAGService:

    def __init__(
        self,
        retriever,
        context_builder,
        llm_service,
    ):
        self.retriever = retriever
        self.context_builder = context_builder
        self.llm_service = llm_service

    def answer(
        self,
        question: str,
        document_id: int | None = None,
        score_threshold: float | None = None,
    ) -> dict:

        results = self.retriever.search(
            query=question,
            limit=5,
            document_id=document_id,
            score_threshold=score_threshold,
        )

        if not results:

            return {
                "answer": (
                    "I could not find the answer "
                    "in the provided documents."
                ),
                "sources": [],
            }

        context = self.context_builder.build(
            results
        )

        prompt = SYSTEM_PROMPT.format(
            context=context,
            question=question,
        )

        answer = self.llm_service.generate(
            prompt
        )

        sources = []

        for result in results:

            sources.append({
                "document_id": (
                    result.payload["document_id"]
                ),
                "filename": (
                    result.payload["filename"]
                ),
                "page": (
                    result.payload["page"]
                ),
                "score": result.score,
            })

        return {
            "answer": answer,
            "sources": sources,
        }