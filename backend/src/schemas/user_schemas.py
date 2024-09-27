from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    rol: Optional[str] = "empleado"
    plan: Optional[str] = "basico"

class UserCreate(UserBase):
    name: str
    password: str

class UserResponse(UserBase):
    id: int
    name: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str