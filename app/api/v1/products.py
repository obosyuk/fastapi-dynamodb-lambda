from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.services.product_service import ProductService
from app.schemas.product_schema import Product, ProductCreate, ProductUpdate
from app.core.dependencies import get_product_service

router = APIRouter()


@router.get("/", response_model=List[Product])
async def get_all_products(
        service: ProductService = Depends(get_product_service)
):
    """
    Get a list of all products.
    """
    return await service.get_all_products()


@router.get("/{product_id}", response_model=Product)
async def get_product_by_id(
        product_id: str,
        service: ProductService = Depends(get_product_service)
):
    """
    Get details of a product by its ID.
    """
    product = await service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=Product, status_code=201)
async def create_product(
        product_create: ProductCreate,
        service: ProductService = Depends(get_product_service)
):
    """
    Create a new product.
    """
    return await service.create_product(product_create)


@router.put("/{product_id}", response_model=Product)
async def update_product(
        product_id: str,
        product_update: ProductUpdate,
        service: ProductService = Depends(get_product_service)
):
    """
    Update an existing product.
    """
    updated_product = await service.update_product(product_id, product_update)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/{product_id}", status_code=204)
async def delete_product(
        product_id: str,
        service: ProductService = Depends(get_product_service)
):
    """
    Delete a product by its ID.
    """
    success = await service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
