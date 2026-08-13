from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str

    ENV: str

    DEBUG: bool

    DATABASE_URL: str

    REDIS_HOST: str
    REDIS_PORT: int
    
    QDRANT_URL: str
    QDRANT_COLLECTION: str
    VECTOR_SIZE: int

    OPENAI_API_KEY: str

    EMBEDDING_MODEL: str

    CHAT_MODEL: str
    LLM_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()