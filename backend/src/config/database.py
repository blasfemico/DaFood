# backend/src/config/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración directa de la base de datos
DATABASE_URL = "postgresql://postgres:dante20121@localhost/DaFood"
MERCADOPAGO_ACCESS_TOKEN= "TEST-1913182024650502-091621-7b06e528c143a007a993eec7801d14c4-212790061"

# Crear la conexión con la base de datos
engine = create_engine(DATABASE_URL)

# Crear la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
