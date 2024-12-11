import boto3
from app.models.product import ProductModel


class ProductRepository:
    def __init__(self):
        self.table = boto3.resource("dynamodb").Table("Products")

    async def get_all_products(self):
        response = self.table.scan()
        return response.get("Items", [])

    async def get_product_by_id(self, product_id: str):
        response = self.table.get_item(Key={"id": product_id})
        return response.get("Item")

    async def save_product(self, name, description, price, stock):
        product = ProductModel(name=name, description=description, price=price, stock=stock)
        self.table.put_item(Item=product.dict())
        return product

    async def update_product(self, product_id, name=None, description=None, price=None, stock=None):
        # Update logic with conditional expressions for atomicity
        ...

    async def delete_product(self, product_id):
        response = self.table.delete_item(Key={"id": product_id})
        return response.get("ResponseMetadata", {}).get("HTTPStatusCode") == 204
