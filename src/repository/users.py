from typing import Type, Optional

from sqlalchemy.orm import Session

from src.database.models import User, Role
from src.schemas.users import UserBase, UserUpdate


async def get_user_by_email(email: str, db: Session) -> Type[User] | None:
    """
    The get_user_by_email function takes in an email and a database session,
    and returns the user associated with that email. If no such user exists, it returns None.

    :param email: str: Pass the email address of the user to be retrieved
    :param db: Session: Pass the database session to the function
    :return: The first user with the given email, or none if no such user exists
    """
    return db.query(User).filter(User.email == email).first()


async def update_user(body: UserUpdate, user: User, db: Session) -> User:
    """
    The update_user function updates a user in the database.

    :param body: UserUpdate: Get the data from the request body
    :param user: User: Get the user from the database
    :param db: Session: Access the database
    :return: The updated user
    """
    user.first_name = body.first_name
    user.last_name = body.last_name
    user.birthday = body.birthday
    user.job = body.job
    user.phone = body.phone

    db.commit()
    db.refresh(user)
    return user


async def update_avatar(email: str, url: str, db: Session) -> Type[User] | None:
    """
    The update_avatar function updates the avatar of a user in the database.

    :param email: str: Identify the user
    :param url: str: Update the avatar url of a user
    :param db: Session: Pass the database session to the function
    :return: A user object, or none if the user was not found
    """
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user


async def create_user(body: UserBase, db: Session) -> User:
    """
    The create_user function creates a new user in the database.

    :param body: UserBase: Define the data that is passed in to the function
    :param db: Session: Pass the database session to the function
    :return: The new user
    :doc-author: Trelent
    """
    new_user = User(**body.dict(), role=Role(name="user"))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: Optional[str], db: Session) -> None:
    """
    The update_token function updates the refresh token for a user.

    :param user: User: Get the user's id
    :param token: Optional[str]: Specify that the token parameter is optional
    :param db: Session: Pass the database session to the function
    :return: None
    """
    user.refresh_token = token
    db.commit()
    
    
async def confirmed_email(user: User, db: Session) -> None:
    """
    The confirmed_email function is called when a user confirms their email address.
    It sets the confirmed field of the User object to True, and commits it to the database.

    :param user: User: Pass the user object to the function
    :param db: Session: Access the database
    :return: None, because it does not have a return statement
    """
    user.confirmed = True
    db.commit()
    
    
async def save_new_password(user: User, password_hash: str, db: Session) -> None:
    """
    The save_new_password function takes a user object, a password hash, and the database session as arguments.
    It then sets the user's password to be equal to the new password hash.
    Finally, it commits this change to the database.

    :param user: User: Get the user object from the database
    :param password_hash: str: Pass in the hashed password
    :param db: Session: Pass the database session to the function
    :return: None
    """
    user.password = password_hash
    db.commit()
