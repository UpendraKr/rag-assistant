from app.services.langchain_retriever import retriever


documents = retriever.invoke(
    "What is ranking of iit delhi in 2021 for engineering?"
)


for document in documents:

    print("\n" + "=" * 60)

    print("CONTENT:")
    print(document)

    print("\nMETADATA:")
    print(document.metadata)