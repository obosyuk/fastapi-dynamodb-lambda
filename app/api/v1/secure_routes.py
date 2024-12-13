from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter()


@router.get("/")
def secure_data(user: dict = Depends(get_current_user)):
    return {"message": "This is protected data", "user": user}
