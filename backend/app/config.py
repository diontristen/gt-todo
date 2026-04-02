from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://todo_user:todo_pass@db:5432/todo_app"

    model_config = {"env_file": ".env"}


settings = Settings()
