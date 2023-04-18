from unittest.mock import MagicMock, AsyncMock

import pytest

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


def test_create_group_forbidden(client, token):
    response = client.post(
        "api/groups",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Family"}
    )

    assert response.status_code == 403, response.text
    data = response.json()
    assert data["detail"] == "Does not have access"


def test_update_group_user(client, session, user, token):
    response = client.put(
        "api/groups/1",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Home"}
    )

    assert response.status_code == 403, response.text
    data = response.json()
    assert data["detail"] == "Does not have access"


def test_remove_group_user(client, session, user, token):
    response = client.delete(
        "api/groups/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 403, response.text
    data = response.json()
    assert data["detail"] == "Does not have access"


def test_update_group_not_found(client, session, user, token):
    current_user = get_current_user(user, session)
    current_user.role = Role(name="admin")
    session.commit()

    response = client.put(
        "api/groups/1",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Home"}
    )

    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Group not found"


def test_remove_group_not_found(client, session, user, token):
    response = client.delete(
        "api/groups/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Group not found"


def test_create_group(client, session, user, token):
    response = client.post(
        "api/groups",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Family"}
    )

    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "Family"
    assert "id" in data


def test_update_group_admin(client, token):
    response = client.put(
        "api/groups/1",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Home"}
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Home"
    assert "id" in data


def test_read_groups(client, token, monkeypatch):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())
    response = client.get(
        "api/groups",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["name"] == "Home"
    assert "id" in data[0]


def test_read_group(client, token, monkeypatch):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())
    response = client.get(
        "api/groups/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Home"
    assert "id" in data


def test_read_group_2(client, token, monkeypatch):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())
    response = client.get(
        "api/groups/2",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Group not found"


def test_remove_group(client, session, user, token):
    response = client.delete(
        "api/groups/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 202, response.text
    data = response.json()
    assert data["name"] == "Home"
    assert "id" in data
