from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ItemBase(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    price: float

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: UUID
    name: str
    description: Optional[str] = None,
    price: float

    class Config:
        orm_mode = True
