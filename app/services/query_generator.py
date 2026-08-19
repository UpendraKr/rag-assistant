from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from app.core.config import settings
from app.prompts.multi_query import MULTI_QUERY_PROMPT


class QueryGenerator:

    def __init__(self):

        self.llm = ChatOpenAI(
            model=settings.LLM_MODEL,
            temperature=0,
            api_key=settings.OPENAI_API_KEY
        )

        self.chain = (
            MULTI_QUERY_PROMPT
            | self.llm
            | StrOutputParser()
        )

    def generate(self, question: str) -> list[str]:

        response = self.chain.invoke(
            {
                "question": question,
            }
        )

        queries = [
            query.strip()
            for query in response.splitlines()
            if query.strip()
        ]

        return queries[:4]