from datetime import UTC, datetime

from app.repositories.order_repository import OrderRepository
from app.schemas.order_schema import Order, OrderCreate


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    async def create_order(self, order_create: OrderCreate) -> Order:
        order = await self.repository.save_order(
            user_id=order_create.user_id,
            total_price=order_create.total_price,
            status=order_create.status,
        )
        return Order(
            id=order.id,
            user_id=order.user_id,
            total_price=order.total_price,
            status=order.status,
            created_at=datetime.now(UTC),
            updated_at=None,
        )
