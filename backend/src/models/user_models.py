from sqlalchemy import Column, Integer, String, Boolean
from ..config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    rol = Column(String, default="empleado")  # Agregar campo de rol
    plan = Column(String, default="basico")  # Agregar campo de plan
    is_superuser = Column(Boolean, default=False)
