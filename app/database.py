# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.config import settings

Base = declarative_base()

def get_engine(database_url: str = None):
    """Factory to create an engine with a given or default database URL."""
    url = database_url or settings.DATABASE_URL
    return create_engine(url)

def get_sessionmaker(engine=None):
    """Factory to create a sessionmaker bound to an engine."""
    eng = engine or get_engine()
    return sessionmaker(autocommit=False, autoflush=False, bind=eng)

# Default instances
engine = get_engine()
SessionLocal = get_sessionmaker(engine=engine)

def get_db():
    """Dependency for injecting database sessions into route handlers."""
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError:
        db.rollback()
        raise
    finally:
        db.close()