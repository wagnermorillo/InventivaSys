import dotenv, os
from .models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .seedData import SeedData

dbPath = "db.sqlite3"
FULL_URL_BD = f"sqlite:///{dbPath}"

# Configurar la base de datos
engine = create_engine(FULL_URL_BD)
Base.metadata.create_all(engine)

# crear session
Session = sessionmaker(bind=engine)
session = Session()
SeedData(session)