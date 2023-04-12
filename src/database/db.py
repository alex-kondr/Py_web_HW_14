from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.conf.config import settings


db_url = "postgresql://gkofooxx:cqeFSr15Em1MIi-2cJVme9GfsdBZzh5b@snuffleupagus.db.elephantsql.com/gkofooxx"
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    The get_db function is a context manager that returns the database session.
    It also ensures that the connection to the database is closed after each request.

    :return: A database sessionlocal object
    :doc-author: Trelent
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()