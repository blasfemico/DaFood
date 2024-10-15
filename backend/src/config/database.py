# backend/src/config/database.py
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Verificar si el archivo .env existe, si no, crearlo
env_path = Path('.') / '.env'
if not env_path.exists():
    with open(env_path, 'w') as f:
        f.write("DATABASE_URL=postgresql://postgres:dante20121@localhost/DaFood\n")
        f.write("MERCADOPAGO_ACCESS_TOKEN=TEST-1913182024650502-091621-7b06e528c143a007a993eec7801d14c4-212790061\n")

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos usando variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
MERCADOPAGO_ACCESS_TOKEN = os.getenv("MERCADOPAGO_ACCESS_TOKEN")

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
