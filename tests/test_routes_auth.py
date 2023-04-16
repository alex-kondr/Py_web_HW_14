import unittest
from unittest.mock import MagicMock

from src.database.models import User


def get_current_user(user, session):
    current_user: User = session.query(User).filter(User.email == user.get("email")).first()
    return current_user


def test_create_user(client, user, monkeypatch):
    monkeypatch.setattr("src.routes.auth.send_email", MagicMock())
    response = client.post(
        "api/auth/singup",
        json=user,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["user"]["email"] == user.get("email")
    assert data["user"]["username"] == user.get("username")
    assert "id" in data["user"]


def test_repeate_create_user(client, user):
    response = client.post(
        "api/auth/singup",
        json=user,
    )
    assert response.status_code == 409, response.text
    data = response.json()
    assert data["detail"] == "Account already exists"


def test_login_user_not_confirmed(client, user):
    response = client.post(
        "api/auth/login",
        data={
            "username": user.get("email"),
            "password": user.get("password")
        }
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] == "Email not confirmed"


def test_login_is_not_valid_email(client):
    response = client.post(
        "api/auth/login",
        data={
            "username": "username",
            "password": "password"
        }
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] == "Invalid email"


def test_request_email(client, user, monkeypatch):
    monkeypatch.setattr("src.routes.auth.send_email", MagicMock())
    response = client.post(
        "/api/auth/request_email",
        json=user,
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "Check your email for confirmation."


def test_request_email_not_found(client, user_two, monkeypatch):
    monkeypatch.setattr("src.routes.auth.send_email", MagicMock())
    response = client.post(
        "/api/auth/request_email",
        json=user_two,
    )

    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"


def test_login_is_not_valid_password(client, session, user):
    current_user = get_current_user(user, session)
    current_user.confirmed = True
    session.commit()
    response = client.post(
        "api/auth/login",
        data={
            "username": user.get("email"),
            "password": "password"
        }
    )
    assert response.status_code == 401, response.text
    data = response.json()
    assert data["detail"] == "Invalid password"


def test_request_email_already_confirmed(client, user):
    response = client.post(
        "/api/auth/request_email",
        json=user,
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "You email is already confirmed"


def test_login_user(client, user):
    response = client.post(
        "api/auth/login",
        data={
            "username": user.get("email"),
            "password": user.get("password")
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["token_type"] == "bearer"
    assert "access_token" in data
    assert "refresh_token" in data


def test_refresh_token(client, session, user):
    current_user = get_current_user(user, session)
    response = client.get(
        "api/auth/refresh_token",
        headers={
            "Authorization": f"Bearer {current_user.refresh_token}"
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["token_type"] == "bearer"
    assert "access_token" in data
    assert "refresh_token" in data


def test_not_valid_refresh_token(client, session, user):
    current_user = get_current_user(user, session)
    refresh_token = current_user.refresh_token
    current_user.refresh_token = "refresh_token"
    session.commit()
    
    response = client.get(
        "api/auth/refresh_token",
        headers={
            "Authorization": f"Bearer {refresh_token}"
        }
    )
    assert response.status_code == 401, response.text
    data = response.json()
    current_user = get_current_user(user, session) 
    assert data["detail"] == "Invalid refresh token"
    assert current_user.refresh_token is None
  
    
def test_forgot_password_not_found(client, user_two):
    response = client.post(
        "api/auth/forgot_password",
        json=user_two
    )
    
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"
 

def test_forgot_password(client, user, monkeypatch):
    monkeypatch.setattr("src.routes.auth.send_email", MagicMock())
    response = client.post(
        "api/auth/forgot_password",
        json=user
    )
    
    assert response.status_code == 200, response.text
    data = response.json()
    email = user.get("email")
    assert data["message"] == f"Further instructions have been sent to e-mail ({email})."


def test_forgot_password_email_not_confirmed(user, session, client):
    current_user = get_current_user(user, session)
    current_user.confirmed = False
    
    response = client.post(
        "api/auth/forgot_password",
        json=user
    ) 
    
    assert response.status_code == 403, response.text
    data = response.json()
    assert data["detail"] == "Email not confirmed"
 