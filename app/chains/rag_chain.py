from langchain_core.output_parsers import (
    StrOutputParser,
)
from langchain_core.prompts import (
    ChatPromptTemplate,
)

from langchain_core.runnables import (
    RunnablePassthrough,
)

from langchain_openai import ChatOpenAI

from app.core.config import settings

from app.services.langchain_retriever import (
    retriever,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a document question-answering assistant.

            Answer the question using ONLY the
            provided context.

            If the answer cannot be found in the
            context, say:

            "I could not find the answer in the
            provided documents."

            Context:

            {context}
            """,
        ),
        (
            "human",
            "{question}",
        ),
    ]
)

def format_documents(documents):

    return "\n\n---\n\n".join(
        document.page_content
        for document in documents
    )


llm = ChatOpenAI(
    model=settings.LLM_MODEL,
    api_key=settings.OPENAI_API_KEY,
    temperature=0,
)

rag_chain = (
    {
        "context": retriever | format_documents,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)