from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
)
from langchain_openai import ChatOpenAI
from app.core.config import settings


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a document question-answering assistant.

            Answer only using the provided context.

            If the answer is not present in the
            context, say:

            "I could not find the answer in
            the provided documents."

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


llm = ChatOpenAI(
    model=settings.LLM_MODEL,
    temperature=0,
    api_key=settings.OPENAI_API_KEY,
)

chain = (
    prompt
    | llm
    | StrOutputParser()
)

answer = chain.invoke(
    {
        "context": "...",
        "question": "What is RAG?",
    }
)