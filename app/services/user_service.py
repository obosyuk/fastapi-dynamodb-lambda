from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, User


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, user_create: UserCreate) -> User:
        user = await self.repository.save_user(user_create.username, user_create.email)
        return User(id=user.id, username=user.username, email=user.email)
