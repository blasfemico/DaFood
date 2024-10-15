from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models.user_models import User
from ..schemas.user_schemas import UserCreate
from passlib.context import CryptContext

# Crear un contexto de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        hashed_password = pwd_context.hash(user.password)
        db_user = User(
            name=user.name,
            email=user.email,
            hashed_password=hashed_password,
            rol=user.rol or "empleado",  
            plan=user.plan or "basico"   
        )
        try:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo electrónico ya está registrado.",
            )

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> User:
        user = db.query(User).filter(User.email == email).first()
        if not user or not pwd_context.verify(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def update_user_plan(db: Session, user_id: int, new_plan: str, current_user: User) -> User:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

        if new_plan in ["intermedio", "avanzado"] and current_user.rol != "admin":  
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para cambiar al plan superior.")

        user.plan = new_plan
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
        return user
