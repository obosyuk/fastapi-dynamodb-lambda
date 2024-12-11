from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str = Field(..., description="Name of the product")
    description: Optional[str] = Field(None, description="Short description of the product")
    price: float = Field(..., gt=0, description="Price of the product")
    stock: int = Field(..., ge=0, description="Stock available for the product")


class ProductCreate(ProductBase):
    """
    Schema for creating a new product.
    """
    pass


class ProductUpdate(BaseModel):
    """
    Schema for updating an existing product.
    """
    name: Optional[str]
    description: Optional[str]
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)


class Product(ProductBase):
    """
    Schema for returning product data.
    """
    id: str = Field(..., description="The unique identifier of the product")
    created_at: datetime = Field(..., description="The timestamp when the product was created")
    updated_at: Optional[datetime] = Field(None, description="The timestamp when the product was last updated")

    class Config:
        orm_mode = True
