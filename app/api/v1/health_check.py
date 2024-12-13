from fastapi import APIRouter
from app.core.logging import setup_logging

logger = setup_logging()

router = APIRouter()


@router.get("/health")
async def health_check():
    logger.info(f"Health check has been requested")
    return {"status": "healthy"}
