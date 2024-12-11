from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "E-Commerce API"
    aws_region: str
    dynamodb_endpoint: str = None  # Optional for local testing

    class Config:
        env_file = ".env"


settings = Settings()
