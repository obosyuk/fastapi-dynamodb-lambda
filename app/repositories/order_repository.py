from app.models.order import OrderModel
import boto3
import uuid


class OrderRepository:
    def __init__(self):
        self.table = boto3.resource("dynamodb").Table("Orders")

    async def save_order(self, user_id: str, total_price: float, status: str) -> OrderModel:
        order_id = str(uuid.uuid4())
        order = OrderModel(id=order_id, user_id=user_id, total_price=total_price, status=status)
        self.table.put_item(Item=order.__dict__)
        return order
