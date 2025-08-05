from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class UserCreate(BaseModel):
    id: UUID
    username: str
    password: str
    role: Optional[str] = "user"

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: UUID
    username: str
    role: str

    class Config:
        orm_mode = True
