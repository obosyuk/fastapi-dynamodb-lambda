from fastapi import APIRouter, Depends

from app.core.dependencies import get_order_repository
from app.schemas.order_schema import Order, OrderCreate
from app.services.order_service import OrderService

router = APIRouter()


@router.post("/", response_model=Order)
async def create_order(
    order: OrderCreate,
    order_service: OrderService = Depends(lambda: OrderService(get_order_repository())),
):
    return await order_service.create_order(order)
