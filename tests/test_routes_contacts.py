from unittest.mock import AsyncMock, MagicMock

import pytest

from src.database.models import User


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


def test_create_contact(client, token, monkeypatch, contact):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())

    response = client.post(
        "api/contacts",
        headers={"Authorization": f"Bearer {token}"},
        json=contact
    )

    assert response.status_code == 201, response.text
    data = response.json()
    assert data["first_name"] == contact["first_name"]
    assert data["last_name"] == contact["last_name"]
    assert data["phone"] == contact["phone"]
    assert "id" in data


def test_read_contacts(client, token, monkeypatch, contact):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())

    response = client.get(
        "api/contacts",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["first_name"] == contact["first_name"]
    assert data[0]["last_name"] == contact["last_name"]
    assert data[0]["phone"] == contact["phone"]
    assert "id" in data[0]


def test_read_contact(client, token, monkeypatch, contact):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())

    response = client.get(
        "api/contacts/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["first_name"] == contact["first_name"]
    assert data["last_name"] == contact["last_name"]
    assert data["phone"] == contact["phone"]
    assert "id" in data


def test_read_contact_not_found(client, token, monkeypatch, contact):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())

    response = client.get(
        "api/contacts/2",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Contact not found"


def test_find_contact(client, token, monkeypatch, contact):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())

    response = client.get(
        f"api/contacts/find?first_name=first_name",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["first_name"] == contact["first_name"]
    assert data[0]["last_name"] == contact["last_name"]
    assert data[0]["phone"] == contact["phone"]
    assert "id" in data[0]


def test_not_find_contact(client, token, monkeypatch, contact):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())

    response = client.get(
        f"api/contacts/find?first_name=first",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Contact not found"


def test_update_contact(client, token, monkeypatch, contact_update):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())
    monkeypatch.setattr("src.services.auth.auth_service.r.keys", AsyncMock(return_value=None))

    response = client.put(
        "api/contacts/1",
        headers={"Authorization": f"Bearer {token}"},
        json=contact_update
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["first_name"] == contact_update["first_name"]
    assert data["last_name"] == contact_update["last_name"]
    assert data["phone"] == contact_update["phone"]
    assert "id" in data


def test_update_contact_not_found(client, token, monkeypatch, contact_update):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())

    response = client.put(
        "api/contacts/2",
        headers={"Authorization": f"Bearer {token}"},
        json=contact_update
    )

    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Contact not found"


def test_remove_contact(client, token, monkeypatch, contact_update):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())
    monkeypatch.setattr("src.services.auth.auth_service.r.keys", AsyncMock(return_value=None))

    response = client.delete(
        "api/contacts/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 202, response.text
    data = response.json()
    assert data["first_name"] == contact_update["first_name"]
    assert data["last_name"] == contact_update["last_name"]
    assert data["phone"] == contact_update["phone"]
    assert "id" in data


def test_remove_contact_not_found(client, token, monkeypatch, contact_update):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())

    response = client.delete(
        "api/contacts/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Contact not found"
