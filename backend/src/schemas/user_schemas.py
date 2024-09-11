from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    rol: Optional[str] = "empleado"  # Añadido: campo opcional rol, con valor por defecto "empleado"
    plan: Optional[str] = "basico"   # Añadido: campo opcional plan, con valor por defecto "básico"

class UserCreate(UserBase):
    name: str
    password: str

class UserResponse(UserBase):
    id: int
    name: str

    class Config:
        from_attributes = True  # Para que Pydantic use los atributos del modelo ORM

class UserLogin(BaseModel):
    email: EmailStr
    password: str
