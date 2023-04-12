from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    password: str = Field(min_length=6, max_length=10)


class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: str = Field(min_length=5, max_length=16)
    birthday: Optional[date]
    job: Optional[str]
    email: Optional[EmailStr]
    phone: str = Field(regex=r"^(\+)[1-9][0-9\-\(\)]{9,16}$")


class UserModel(UserBase, UserUpdate):
    pass


class UserDB(UserUpdate):
    id: int
    created_at: datetime
    avatar: Optional[str]

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDB
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr


class UpdatePassword(BaseModel):
    password: str = Field(min_length=6, max_length=10)
