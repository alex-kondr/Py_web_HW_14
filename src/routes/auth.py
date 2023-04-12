from fastapi import APIRouter, HTTPException, Depends, status, Security, BackgroundTasks, Request
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas.users import UserModel, UserResponse, TokenModel, RequestEmail, UpdatePassword
from src.repository import users as repository_users
from src.services.auth import auth_service
from src.services.email import send_email


router = APIRouter(prefix="/auth", tags=["auth"])
security = HTTPBearer()


@router.post("/singup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def singup(body: UserModel,
                 background_tasks: BackgroundTasks,
                 request: Request,
                 db: Session = Depends(get_db)) -> dict:
    """
    The singup function creates a new user in the database.
        It takes an email, username and password as input parameters.
        The function returns a JSON object with the newly created user's information.

    :param body: UserModel: Validate the data sent by the user
    :param background_tasks: BackgroundTasks: Add a task to the background tasks queue
    :param request: Request: Get the host url to send in the email
    :param db: Session: Get the database session
    :return: A dictionary with the user and a message
    """
    exist_user = await repository_users.get_user_by_email(body.email, db)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    body.password = auth_service.get_password_hash(body.password)
    new_user = await repository_users.create_user(body, db)
    
    background_tasks.add_task(send_email, email=new_user.email, 
                              subject="Confirm email", 
                              template_name="email_template.html", 
                              username=new_user.username, 
                              host=request.base_url)
    return {"user": new_user, "detail": "User successfully created."}


@router.post("/login", response_model=TokenModel)
async def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> dict:
    """
    The login function is used to authenticate a user.
        It takes in the username and password of the user, and returns an access token if successful.
        The access token can be used to make requests on behalf of that user.

    :param body: OAuth2PasswordRequestForm: Get the username and password from the request body
    :param db: Session: Access the database
    :return: A dictionary with the access token, refresh token and bearer
    """
    user = await repository_users.get_user_by_email(body.username, db)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    if not user.confirmed:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email not confirmed")
    if not auth_service.verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
    access_token: str = await auth_service.create_access_token(data={"sub": user.email})
    refresh_token: str = await auth_service.create_refresh_token(data={"sub": user.email})
    await auth_service.get_current_user(access_token, db)
    await repository_users.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get("/refresh_token", response_model=TokenModel)
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security),
                        db: Session = Depends(get_db)) -> dict:
    """
    The refresh_token function is used to refresh the access token.
        The function takes in a refresh token and returns an access_token, a new refresh_token, and the type of token.

    :param credentials: HTTPAuthorizationCredentials: Get the access token from the request header
    :param db: Session: Get the database session
    :return: A dictionary with the new access_token, refresh_token and token type
    """
    token = credentials.credentials
    email = await auth_service.decode_refresh_token(token)
    user = await repository_users.get_user_by_email(email, db)
    if user.refresh_token != token:
        await repository_users.update_token(user, None, db)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    
    access_token: str = await auth_service.create_access_token(data={"sub": email})
    refresh_token: str = await auth_service.create_refresh_token(data={"sub": email})
    await repository_users.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get("/confirmed_email/{token}")
async def confirmed_email(token: str, db: Session = Depends(get_db)) -> dict:
    """
    The confirmed_email function is used to confirm a user's email address.
        It takes in the token that was sent to the user's email and checks if it is valid.
        If it is, then we set the confirmed field of that user to True.

    :param token: str: Get the email and type from the token
    :param db: Session: Get the database session
    :return: The message that the email has been confirmed
    """
    email, type_ = await auth_service.get_email_type_from_token(token)
    user = await repository_users.get_user_by_email(email, db)
    
    if type_ != "Confirm email" or user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
    if user.confirmed:
        return {"message": "You email is already confirmed"}
    await repository_users.confirmed_email(user, db)
    return {"message": "Email confirmed"}


@router.post("/request_email")
async def request_email(body: RequestEmail, 
                        background_tasks: BackgroundTasks, 
                        request: Request,
                        db: Session = Depends(get_db)) -> dict:
    
    """
    The request_email function is used to send a confirmation email to the user.
        The function takes in an email address and sends a confirmation link to that
        address. If the user does not exist, it returns an error message.

    :param body: RequestEmail: Validate the request body
    :param background_tasks: BackgroundTasks: Add a task to the background tasks queue
    :param request: Request: Get the base_url of the application
    :param db: Session: Pass the database session to the repository functions
    :return: A message to the user if they are already confirmed
    """
    user = await repository_users.get_user_by_email(body.email, db)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
    if user.confirmed:
        return {"message": "You email is already confirmed"}
    
    background_tasks.add_task(send_email, email=user.email, 
                                subject="Confirm email", 
                                template_name="email_template.html.html", 
                                username=user.username, 
                                host=request.base_url)
    return {"message": "Check your email for confirmation."}


@router.post("/forgot_password")
async def forgot_password(body: RequestEmail,
                          background_tasks: BackgroundTasks, 
                          request: Request,
                          db: Session = Depends(get_db)) -> dict:
    
    """
    The forgot_password function is used to send an email to the user with a link
    to reset their password. The function takes in a RequestEmail object, which contains
    the user's email address. It then checks if the user exists and if they have confirmed
    their account (if not, it raises an exception). If everything is okay, it sends them
    an email with instructions on how to reset their password.

    :param body: RequestEmail: Get the email from the request body
    :param background_tasks: BackgroundTasks: Add a task to the background tasks queue
    :param request: Request: Get the base_url of the application
    :param db: Session: Get the database session
    :return: A dict with a message
    """
    user = await repository_users.get_user_by_email(body.email, db)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not user.confirmed:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email not confirmed")
    
    background_tasks.add_task(send_email, email=user.email, 
                              subject="Reset password", 
                              template_name="reset_password.html", 
                              username=user.username, 
                              host=request.base_url)
    
    return {"message": f"Further instructions have been sent to e-mail ({body.email})."}


@router.post("/reset_password/{token}")
async def reset_password(token: str, body: UpdatePassword, db: Session = Depends(get_db)) -> dict:
    """
    The reset_password function takes a token and a body as arguments.
    The token is used to verify the user's email address, while the body contains the new password.
    If verification fails, an HTTP 400 error is raised. Otherwise, the function saves
    the new password in database.

    :param token: str: Get the email and type of token from the database
    :param body: UpdatePassword: Get the new password from the user
    :param db: Session: Pass the database session to the function
    :return: A dict with a message
    """
    email, type_ = await auth_service.get_email_type_from_token(token)
    user = await repository_users.get_user_by_email(email, db)
    
    if type_ != "Reset password" or user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
    
    password_hash = auth_service.get_password_hash(body.password)
    await repository_users.save_new_password(user, password_hash, db)
    return {"message": "Password updated"}