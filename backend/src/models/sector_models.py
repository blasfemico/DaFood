from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from  ..config.database import Base

class Sector(Base):
    __tablename__ = "sectores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    
    mesas = relationship("Mesa", back_populates="sector")


class Mesa(Base):
    __tablename__ = "mesas"

    id = Column(Integer,primary_key=True,index=True)
    Mesas = Column(Integer, index=True)
    sector_id = Column(Integer, ForeignKey("sectores.id"))

    sector = relationship ("Sector", back_populates="mesas")

