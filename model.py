from pydantic import BaseModel
from uuid import UUID


# products schema
class Product(BaseModel):
    id: UUID
    name: str
    model_id: str
    description: str
    price: int
    

# categories schema
class Category(BaseModel):
    id: int
    name: str


# brands schema
class Brand(BaseModel):
    id: int
    name: str