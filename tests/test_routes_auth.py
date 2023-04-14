from unittest.mock import MagicMock

from src.database.models import User


def test_create_user(client, user, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    response = client.post(
        "api/auth/singup",
        json=user,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["user"]["email"] == user.get("email")
    assert data["user"]["username"] == user.get("username")
    assert "id" in data["user"]


# def test_create_user_two(client, user_two, monkeypatch):
#     mock_send_email = MagicMock()
#     monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
#     response = client.post(
#         "api/auth/singup",
#         json=user_two,
#     )
#     assert response.status_code == 201, response.text
#     data = response.json()
#     assert data["user"]["email"] == user_two.get("email")
#     assert data["user"]["username"] == user_two.get("username")
#     assert "id" in data["user"]


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


def test_login_is_not_valid_email(client, user):
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
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    response = client.post(
        "/api/auth/request_email",
        json=user,
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == "Check your email for confirmation."


def test_request_email_not_found(client, user_two, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    response = client.post(
        "/api/auth/request_email",
        json=user_two,
    )

    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"


def test_login_is_not_valid_password(client, session, user):
    current_user: User = session.query(User).filter(User.email == user.get("email")).first()
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


def test_request_email_alreade_confirmed(client, user, monkeypatch):
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


# def test_login_user_two(client, user_two):
#     response = client.post(
#         "api/auth/login",
#         data={
#             "username": user_two.get("email"),
#             "password": user_two.get("password")
#         }
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["token_type"] == "bearer"


def test_refresh_token(client, session, user):
    current_user: User = session.query(User).filter(User.email == user.get("email")).first()
    response = client.get(
        "api/auth/refresh_token",
        headers={
            "Authorization": f"Bearer {current_user.refresh_token}"
        }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["token_type"] == "bearer"


# def test_not_valid_refresh_token(client, session, user):
#     current_user: User = session.query(User).filter(User.email == user.get("email")).first()
#     refresh_token = current_user.refresh_token
#     response = client.get(
#         "api/auth/refresh_token",
#         headers={
#             "Authorization": f"Bearer {refresh_token}"
#         }
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["token_type"] == "bearer"
#     assert data["refresh_token"] != refresh_token
#
#     response = client.get(
#         "api/auth/refresh_token",
#         headers={
#             "Authorization": f"Bearer {refresh_token}"
#         }
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     print(f"{data=}")
#     assert data["detail"] == "Invalid refresh token"
#     assert data["token_type"] is None


# def test_confirmed_email():
#     pass




