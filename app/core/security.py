import requests
from fastapi import HTTPException, Request
from jose import JWTError, jwt
from pydantic import BaseModel

from app.core.config import settings
from app.core.logging import setup_logging

logger = setup_logging()


class User(BaseModel):
    user_id: str
    groups: list[str]


# Cognito JWKS URL
COGNITO_JWKS_URL = (
    f"https://cognito-idp.{settings.aws_region}.amazonaws.com/"
    f"{settings.aws_cognito_user_pool_id}/.well-known/jwks.json"
)

# Fetch JWKS
response = requests.get(COGNITO_JWKS_URL)
JWKS = response.json()


def decode_token(token: str):
    try:
        headers = jwt.get_unverified_headers(token)
        print(headers)
        kid = headers.get("kid")
        print(JWKS)
        key = next((key for key in JWKS["keys"] if key["kid"] == kid), None)
        if not key:
            raise HTTPException(status_code=403, detail="Invalid token")

        decoded_token = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            audience=settings.aws_cognito_app_client_id,
            issuer=f"https://cognito-idp.{settings.aws_region}.amazonaws.com/{settings.aws_cognito_user_pool_id}",
        )
        return decoded_token
    except JWTError as e:
        logger.error(e)
        raise HTTPException(status_code=403, detail="Token validation failed")


def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    token = auth_header.split(" ")[1]
    return decode_token(token)
