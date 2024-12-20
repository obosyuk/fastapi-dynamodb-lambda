from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class OrderBase(BaseModel):
    user_id: str = Field(..., description="The ID of the user who placed the order")
    total_price: float = Field(..., gt=0, description="Total price of the order")
    status: str = Field(
        ..., description="Status of the order (e.g., 'pending', 'completed')"
    )


class OrderCreate(OrderBase):
    """
    Schema for creating a new order.
    """

    pass


class OrderUpdate(BaseModel):
    """
    Schema for updating an existing order.
    """

    total_price: Optional[float] = Field(
        None, gt=0, description="Updated total price of the order"
    )
    status: Optional[str] = Field(None, description="Updated status of the order")


class Order(OrderBase):
    """
    Schema for returning order data.
    """

    id: str = Field(..., description="The unique identifier of the order")
    created_at: datetime = Field(
        ..., description="The timestamp when the order was created"
    )
    updated_at: Optional[datetime] = Field(
        None, description="The timestamp when the order was last updated"
    )

    class Config:
        orm_mode = True
