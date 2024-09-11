from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas.sector_schemas import SectorCreate, Sector, MesaCreate, Mesa
from ...services.sector_services import SectorService
from ...config.database import get_db
from ...middleware.AMW import AuthMiddleware  # Asegúrate de tener un middleware de autenticación
from ...models.user_models import User

router = APIRouter()

auth_middleware = AuthMiddleware()

@router.post("/sectores", response_model=Sector)
def create_sector(sector: SectorCreate, db: Session = Depends(get_db)):
    return SectorService.create_sector(db, sector)

@router.get("/sectores", response_model=list[Sector])
def get_sectors(db: Session = Depends(get_db)):
    return SectorService.get_sectors(db)

@router.post("/sectores/{sector_id}/mesas", response_model=Mesa)
def create_mesa(sector_id: int, mesa: MesaCreate, db: Session = Depends(get_db), current_user: User = Depends(auth_middleware.get_current_user)):
    return SectorService.create_mesa(db, mesa, sector_id, current_user)

@router.get("/sectores/{sector_id}/mesas", response_model=list[Mesa])
def get_mesas(sector_id: int, db: Session = Depends(get_db)):
    return SectorService.get_mesas_by_sector(db, sector_id)
