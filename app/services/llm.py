from openai import OpenAI
from app.core.config import settings


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
        self.model = settings.LLM_MODEL

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )
        return response.output_text