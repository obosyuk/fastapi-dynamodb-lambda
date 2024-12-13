from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI DynamoDB App"

    aws_region: str
    aws_cognito_user_pool_id: str
    aws_cognito_app_client_id: str

    class Config:
        env_file = ".env"


settings = Settings()
