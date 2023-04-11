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
async def singup(body: UserModel, background_tasks: BackgroundTasks, request: Request, db: Session = Depends(get_db)):
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
async def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await repository_users.get_user_by_email(body.username, db)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    if not user.confirmed:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email not confirmed")
    if not auth_service.verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
    access_token = await auth_service.create_access_token(data={"sub": user.email})
    refresh_token = await auth_service.create_refresh_token(data={"sub": user.email})
    await auth_service.get_current_user(access_token, db)
    await repository_users.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get("/refresh_token", response_model=TokenModel)
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    email = await auth_service.decode_refresh_token(token)
    user = await repository_users.get_user_by_email(email, db)
    if user.refresh_token != token:
        await repository_users.update_token(user, None, db)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    
    access_token = await auth_service.create_access_token(data={"sub": email})
    refresh_token = await auth_service.create_refresh_token(data={"sub": email})
    await repository_users.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get("/confirmed_email/{token}")
async def confirmed_email(token: str, db: Session = Depends(get_db)):
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
                        db: Session = Depends(get_db)):
    
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
                          db: Session = Depends(get_db)):
    
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
async def reset_password(token: str, body: UpdatePassword, db: Session = Depends(get_db)):
    email, type_ = await auth_service.get_email_type_from_token(token)
    user = await repository_users.get_user_by_email(email, db)
    
    if type_ != "Reset password" or user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
    
    password_hash = auth_service.get_password_hash(body.password)
    await repository_users.save_new_password(user, password_hash, db)
    return {"message": "Password updated"}