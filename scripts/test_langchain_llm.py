from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)
from app.core.config import settings


llm = ChatOpenAI(
    model=settings.LLM_MODEL,
    temperature=0,
    api_key=settings.OPENAI_API_KEY,
)

# use of messages 

# messages = [
#     SystemMessage(
#         content="You are a helpful assistant."
#     ),
#     HumanMessage(
#         content="What is RAG?"
#     ),
# ]
# response = llm.invoke(messages)

# use of prompt template
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a document question-answering assistant.

            Answer only using the provided context.

            If the answer is not present,
            say that you don't know.

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

messages = prompt.invoke(
    {
        "context": "I have a seniour backend engineer with 10 years of experience in Python, Django, and FastAPI. He has worked on various projects involving RESTful APIs, microservices architecture, and cloud deployments. He is also proficient in database design and optimization.",
        "question": "What is the experience of the backend engineer?",
    }
)
response = llm.invoke(messages)

print(response.content)
print("================================")
print(response.__dict__)