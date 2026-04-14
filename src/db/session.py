from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import get_settings

settings = get_settings()
engine = create_engine(url=settings.POSTGRES_DSN)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    """DI DB session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        