from unittest.mock import MagicMock, AsyncMock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from src.database.models import Base, User
from src.database.db import get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def session():
    # Create the database

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client(session):
    # Dependency override

    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)


@pytest.fixture(scope="module")
def user():
    return {"email": "deadpool@example.com", "username": "deadpool", "password": "123456789"}


@pytest.fixture(scope="module")
def user_two():
    return {"email": "dead@example.com", "username": "pooldead", "password": "123456789"}


@pytest.fixture(scope="module")
def contact():
    return {
            "first_name": "first_name",
            "last_name": "last_name",
            "phone": "+38(050)123-45-78"
    }


@pytest.fixture(scope="module")
def contact_update():
    return {
            "first_name": "first_update",
            "last_name": "last_update",
            "phone": "+38(050)111-11-11"
    }
