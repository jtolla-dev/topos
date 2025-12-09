from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/strata"

    # Embeddings (optional)
    enable_embeddings: bool = False
    openai_api_key: str | None = None
    embedding_model: str = "text-embedding-3-small"
    embedding_dimensions: int = 1536

    # Chunking
    chunk_size: int = 1000
    chunk_overlap: int = 200

    # Worker
    worker_poll_interval_seconds: float = 2.0
    worker_max_attempts: int = 3

    # Broad groups for exposure calculation
    broad_group_names: list[str] = [
        "Domain Users",
        "All Employees",
        "Everyone",
        "Authenticated Users",
    ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
