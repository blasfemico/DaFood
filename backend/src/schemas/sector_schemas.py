from pydantic import BaseModel
from typing import List

class MesaBase(BaseModel):
    numero: int

class MesaCreate(MesaBase):
    pass

class Mesa(MesaBase):
    id: int
    sector_id: int

    class Config:
        from_attribute = True

class SectorBase(BaseModel):
    nombre: str

class SectorCreate(SectorBase):
    pass

class Sector(SectorBase):
    id: int
    mesas: List[Mesa] = []

    class Config:
        from_attribute = True
