from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserCreate, User
from app.services.user_service import UserService
from app.core.dependencies import get_user_repository

router = APIRouter()


@router.post("/", response_model=User)
async def create_user(
        user: UserCreate,
        user_service: UserService = Depends(lambda: UserService(get_user_repository()))
):
    return await user_service.create_user(user)
