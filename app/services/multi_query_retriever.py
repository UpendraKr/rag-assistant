from app.services.document_utils import deduplicate_documents

class MultiQueryRetriever:

    def __init__(
        self,
        query_generator,
        retriever,
    ):
        self.query_generator = query_generator
        self.retriever = retriever

    def retrieve(
        self,
        question: str,
    ):

        queries = self.query_generator.generate(
            question
        )

        documents = []

        for query in queries:

            results = self.retriever.invoke(
                query
            )

            documents.extend(results)

        return deduplicate_documents(documents)
        