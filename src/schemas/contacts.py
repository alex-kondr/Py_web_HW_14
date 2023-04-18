from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr

from src.schemas.groups import GroupResponse


class ContactBase(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    phone: str = Field(regex=r"^(\+)[1-9][0-9\-\(\)]{9,16}$")


class ContactModel(ContactBase):
    email: Optional[EmailStr]
    birthday: Optional[date]
    job: Optional[str]
    groups: Optional[List[int]] = []


class ContactUpdate(ContactModel):
    pass


class ContactEmailUpdate(BaseModel):
    email: Optional[EmailStr]


class ContactResponse(ContactModel):
    id: int
    groups: List[GroupResponse]
    avatar: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
