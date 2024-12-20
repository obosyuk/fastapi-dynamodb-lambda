import uuid

import boto3

from app.models.user import UserModel


class UserRepository:
    def __init__(self):
        self.table = boto3.resource("dynamodb").Table("Users")

    async def save_user(self, username: str, email: str) -> UserModel:
        user_id = str(uuid.uuid4())
        user = UserModel(id=user_id, username=username, email=email)
        self.table.put_item(Item=user.__dict__)
        return user
