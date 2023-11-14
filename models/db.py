import dotenv, os
from .models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# cargando las .env
dotenv.load_dotenv()
USER_BD = os.getenv("USERBD")
PASS_BD = os.getenv("PASSBD")
HOST_BD = os.getenv("HOSTBD")
NAME_BD = os.getenv("NAMEBD")
FULL_URL_BD = f"postgresql://{USER_BD}:{PASS_BD}@{HOST_BD}/{NAME_BD}"

# Configurar la base de datos
engine = create_engine(FULL_URL_BD, connect_args={"options": "-c timezone=America/Santo_Domingo"})
Base.metadata.create_all(engine)

# crear session
Session = sessionmaker(bind=engine)
session = Session()