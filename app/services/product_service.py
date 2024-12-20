from app.repositories.product_repository import ProductRepository
from app.schemas.product_schema import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def get_all_products(self):
        return await self.repository.get_all_products()

    async def get_product_by_id(self, product_id: str):
        return await self.repository.get_product_by_id(product_id)

    async def create_product(self, product_create: ProductCreate):
        return await self.repository.save_product(
            name=product_create.name,
            description=product_create.description,
            price=product_create.price,
            stock=product_create.stock,
        )

    async def update_product(self, product_id: str, product_update: ProductUpdate):
        return await self.repository.update_product(
            product_id=product_id,
            name=product_update.name,
            description=product_update.description,
            price=product_update.price,
            stock=product_update.stock,
        )

    async def delete_product(self, product_id: str):
        return await self.repository.delete_product(product_id)
