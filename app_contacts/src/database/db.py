from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.conf.config import settings


db_url = settings.sqlalchemy_database_url
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    
    try:
        yield db
        
    finally:
        db.close()