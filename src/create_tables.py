# create_tables.py
from src.models.user import Base
from src.dependencies.database import engine
import src.models.task  # Ensure Task model is imported so both tables are created

Base.metadata.create_all(bind=engine)