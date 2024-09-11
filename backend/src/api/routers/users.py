from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from ...services.user_services import UserService
from ...schemas.user_schemas import UserCreate, UserResponse
from ...config.database import get_db
from ...middleware.AMW import AuthMiddleware

router = APIRouter()

auth_middleware = AuthMiddleware()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = UserService.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    # Generar el token JWT
    access_token_expires = timedelta(minutes=30)
    access_token = auth_middleware.create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: UserResponse = Depends(auth_middleware.get_current_user)):
    return current_user

@router.patch("/users/{user_id}/plan", response_model=UserResponse)
def update_user_plan(user_id: int, new_plan: str, db: Session = Depends(get_db), current_user: UserResponse = Depends(auth_middleware.get_current_user)):
    # Validamos que solo ciertos usuarios puedan cambiar a "intermedio" o "avanzado"
    return UserService.update_user_plan(db, user_id, new_plan, current_user)

