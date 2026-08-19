from app.services.query_generator import QueryGenerator
from app.services.multi_query_retriever import MultiQueryRetriever
from app.services.langchain_retriever import retriever


multiquery_retriever = MultiQueryRetriever(
    query_generator=QueryGenerator(),
    retriever=retriever,
)


multiquery_documents = multiquery_retriever.retrieve(
    "What is ranking of iit delhi in 2021 for engineering?"
)

print(
    f"Retrieved documents: {len(multiquery_documents)}"
)   


for document in multiquery_documents:
    print("\n------------------")
    print(
        document.page_content[:500]
    )
    print(
        document.metadata
    )