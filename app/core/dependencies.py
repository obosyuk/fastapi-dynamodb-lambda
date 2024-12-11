from fastapi import Depends
from app.repositories.user_repository import UserRepository
from app.repositories.order_repository import OrderRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService


def get_user_repository() -> UserRepository:
    return UserRepository()


def get_order_repository() -> OrderRepository:
    return OrderRepository()


def get_product_repository() -> ProductRepository:
    return ProductRepository()


def get_product_service():
    repository = ProductRepository()
    return ProductService(repository)
