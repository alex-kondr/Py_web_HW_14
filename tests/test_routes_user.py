import io
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import UploadFile

from src.database.models import User, Role


def get_current_user(user, session):
    current_user: User = session.query(User).filter(User.email == user.get("email")).first()
    return current_user


@pytest.fixture()
def token(client, session, user, monkeypatch):
    monkeypatch.setattr("src.routes.auth.send_email", MagicMock())
    monkeypatch.setattr("src.services.auth.auth_service.r.get", AsyncMock(return_value=None))
    monkeypatch.setattr("src.services.auth.auth_service.r.set", AsyncMock())

    client.post("api/auth/singup", json=user)
    current_user = get_current_user(user, session)
    current_user.confirmed = True
    session.commit()

    response = client.post(
        "api/auth/login",
        data={
            "username": user.get("email"),
            "password": user.get("password")
        }
    )
    data = response.json()
    return data["access_token"]


def test_me(client, token, user):
    response = client.get(
        "api/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == user.get("email")


def test_update_profile(client, token):
    response = client.post(
        "api/users",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "first_name": "first_name"
        }
    )

    assert response.status_code == 202, response.text
    data = response.json()
    assert data["first_name"] == "first_name"
