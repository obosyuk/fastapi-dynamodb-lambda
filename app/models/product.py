from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class ProductModel(BaseModel):
    # id: str = Field(default=str(uuid.uuid4()))
    # id: Optional[str] = Field(None, gt=0)
    id: str
    name: str
    price: Decimal
    stock: int
    description: str
    created_at: datetime = Field(default=datetime.now())

    def dict(self, **kwargs):
        item_dict = super().dict(**kwargs)
        # item_dict['id'] = str(uuid.uuid4())
        item_dict["created_at"] = str(item_dict["created_at"].isoformat())
        return item_dict

    # @root_validator(pre=True)
    # def generate_id(cls, values):
    #     if 'id' not in values:  # Check if the ID exists in the values
    #         values['id'] = str(uuid.uuid4())  # Generate a UUID if not
    #     return values

    # class Config:
    #     json_encoders = {
    #         Decimal: lambda v: str(v)
    #     }
