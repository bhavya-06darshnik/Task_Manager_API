from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL) # connect args is only needed for SQLite
# If you are using SQLite, you might want to add connect_args={"check_same_thread": False} to the create_engine call
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()