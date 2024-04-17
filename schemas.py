from pydantic import BaseModel
from uuid import UUID


class Product(BaseModel):
    id: UUID
    name: str
    description: str
    model_name: str
    price: float


class Brand(BaseModel):
    id: int
    name: str


class Category(BaseModel):
    id: int
    name: str

    