# backend/src/api/api.py
from fastapi import APIRouter
from .routers import users, sectores


api_router = APIRouter()

# Agregar el router de usuarios
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(sectores.router, prefix="/sectores", tags=["sectores"])