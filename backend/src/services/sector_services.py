from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.sector_models import Sector, Mesa
from ..models.user_models import User
from ..schemas.sector_schemas import SectorCreate, MesaCreate
from sqlalchemy.exc import SQLAlchemyError

class SectorService:

    # Definir los límites por plan
    LIMITE_POR_PLAN = {
        "basico": 20,  # Límite para plan básico
        "intermedio": 50,  # Límite para plan intermedio
        "avanzado": float('inf')  # Plan avanzado no tiene límite de mesas
    }

    @staticmethod
    def create_sector(db: Session, sector: SectorCreate):
        try:
            db_sector = Sector(nombre=sector.nombre)
            db.add(db_sector)
            db.commit()
            db.refresh(db_sector)
            return db_sector
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail="Error al crear el sector: " + str(e))

    @staticmethod
    def get_sectors(db: Session):
        try:
            return db.query(Sector).all()
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Error al obtener los sectores: " + str(e))

    @staticmethod
    def create_mesa(db: Session, mesa: MesaCreate, sector_id: int, user: User):
        try:
            # Verificar si el sector existe
            sector = db.query(Sector).filter(Sector.id == sector_id).first()
            if not sector:
                raise HTTPException(status_code=404, detail="Sector no encontrado")

            # Obtener el límite del plan del usuario
            limite_mesas = SectorService.LIMITE_POR_PLAN.get(user.plan, 0)

            # Verificar si se ha alcanzado el límite de mesas permitidas según el plan
            num_mesas = db.query(Mesa).filter(Mesa.sector_id == sector_id).count()
            if num_mesas >= limite_mesas:
                raise HTTPException(
                    status_code=400, 
                    detail=f"El límite de mesas para el plan {user.plan} es de {limite_mesas} mesas."
                )

            # Crear la mesa si no se ha alcanzado el límite
            db_mesa = Mesa(numero=mesa.numero, sector_id=sector_id)
            db.add(db_mesa)
            db.commit()
            db.refresh(db_mesa)
            return db_mesa
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail="Error al crear la mesa: " + str(e))

    @staticmethod
    def get_mesas_by_sector(db: Session, sector_id: int):
        sector = db.query(Sector).filter(Sector.id == sector_id).first()
        if not sector:
            raise HTTPException(status_code=404, detail="Sector no encontrado")
        
        return db.query(Mesa).filter(Mesa.sector_id == sector_id).all()

    @staticmethod
    def update_sector(db: Session, sector_id: int, sector_update: SectorCreate):
        sector = db.query(Sector).filter(Sector.id == sector_id).first()
        if not sector:
            raise HTTPException(status_code=404, detail="Sector no encontrado")
        
        sector.nombre = sector_update.nombre
        db.commit()
        db.refresh(sector)
        return sector
