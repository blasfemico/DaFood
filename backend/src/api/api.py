# backend/src/api/api.py
from fastapi import APIRouter
from .routers import users


api_router = APIRouter()

# Agregar el router de usuarios
api_router.include_router(users.router, prefix="/users", tags=["users"])
