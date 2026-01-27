from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    env: str = "development"

    class Config:
        env_file = ".env"
        extra = "forbid"


settings = Settings()
