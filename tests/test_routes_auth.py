from unittest.mock import MagicMock, AsyncMock

from src.database.models import User
from src.services.auth import auth_service


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


def test_login_user(client, user, monkeypatch):
    monkeypatch.setattr("src.services.auth.auth_service.r.get", AsyncMock(return_value=None))
    monkeypatch.setattr("src.services.auth.auth_service.r.set", AsyncMock())
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


def test_reset_password(user, client, session):
    token = auth_service.create_email_token(
        {
            "sub": user.get("email"),
            "type": "Reset password"
        }
    )

    response = client.post(
        f"api/auth/reset_password/{token}",
        json={
            "password": user.get("password")
        }
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "Password updated"


def test_reset_password_invalid_token(user, client, session):
    token = auth_service.create_email_token(
        {
            "sub": user.get("email"),
            "type": "Reset"
        }
    )

    response = client.post(
        f"api/auth/reset_password/{token}",
        json={
            "password": user.get("password")
        }
    )

    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Verification error"


def test_already_confirmed_email(user, client, session):
    token = auth_service.create_email_token(
        {
            "sub": user.get("email"),
            "type": "Confirm email"
        }
    )

    response = client.get(
        f"api/auth/confirmed_email/{token}"
    )

    assert response.status_code == 200, response.text
    data = response.json()
    current_user = get_current_user(user, session)
    assert data["message"] == "You email is already confirmed"
    assert current_user.confirmed is True


def test_confirmed_email(user, client, session):
    current_user = get_current_user(user, session)
    current_user.confirmed = False
    token = auth_service.create_email_token(
        {
            "sub": user.get("email"),
            "type": "Confirm email"
        }
    )

    response = client.get(
        f"api/auth/confirmed_email/{token}"
    )

    assert response.status_code == 200, response.text
    data = response.json()
    current_user = get_current_user(user, session)
    assert data["message"] == "Email confirmed"
    assert current_user.confirmed is True


def test_confirmed_email_invalid_token(user, client, session):
    token = auth_service.create_email_token(
        {
            "sub": user.get("email"),
            "type": "Confirm"
        }
    )

    response = client.get(
        f"api/auth/confirmed_email/{token}"
    )

    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Verification error"
