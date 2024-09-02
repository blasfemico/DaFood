
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta

from ...services.user_services import UserService  
from ...schemas.user_schemas import UserCreate, UserResponse  
from ...models.user_models import User  
from ...config.database import get_db  # Corregido: Importa la función get_db
from ...middleware.AMW import AuthMiddleware  

router = APIRouter()

auth_middleware = AuthMiddleware()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):  # Usar get_db directamente
    db_user = UserService.create_user(db, user)
    return db_user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = UserService.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    access_token_expires = timedelta(minutes=auth_middleware.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_middleware.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(auth_middleware.get_current_user)):
    return current_user
