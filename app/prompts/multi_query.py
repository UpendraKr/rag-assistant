from langchain_core.prompts import ChatPromptTemplate


MULTI_QUERY_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an AI assistant helping with document retrieval.

            Given a user's question, generate multiple alternative
            search queries that capture different ways the question
            could be expressed.

            Generate exactly 4 queries.

            Return ONLY the queries, one per line.
            Do not number them.
            Do not add explanations.
            """,
        ),
        (
            "human",
            "{question}",
        ),
    ]
)