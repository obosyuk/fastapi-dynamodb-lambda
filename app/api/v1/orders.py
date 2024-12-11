from fastapi import APIRouter, Depends
from app.schemas.order_schema import OrderCreate, Order
from app.services.order_service import OrderService
from app.core.dependencies import get_order_repository

router = APIRouter()


@router.post("/", response_model=Order)
async def create_order(
        order: OrderCreate,
        order_service: OrderService = Depends(lambda: OrderService(get_order_repository()))
):
    return await order_service.create_order(order)
