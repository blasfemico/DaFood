from datetime import timedelta, datetime
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..config.database import get_db

# Configuración de JWT y seguridad
SECRET_KEY = "supersecretkey"  # Asegúrate de mover esta clave a una variable de entorno en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

class AuthMiddleware:
    def __init__(self, token: str = Depends(oauth2_scheme)):
        self.token = token
        self.ACCESS_TOKEN_EXPIRE_MINUTES = ACCESS_TOKEN_EXPIRE_MINUTES

    def get_current_user(self, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
        from ..services.user_services import UserService  # Evitar circular importaciones

        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            # Decodificar el token JWT
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: int = payload.get("sub")  # Aquí usamos "sub" para obtener el ID del usuario
            if user_id is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        # Buscar al usuario en la base de datos por ID
        user = UserService.get_user_by_id(db, user_id)  # Cambio para buscar por ID
        if user is None:
            raise credentials_exception

        # Retornar el usuario junto con su plan
        return user

    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
