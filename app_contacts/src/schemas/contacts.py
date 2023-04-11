from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr, constr
from fastapi import UploadFile, File

# from src.database.models import Group, User
from src.schemas.groups import GroupResponse
from src.schemas.users import UserModel


class ContactBase(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    phone: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^(\+)[1-9][0-9\-\(\)]{9,16}$",
        )
    ]
      
        
class ContactModel(ContactBase):
    email: Optional[EmailStr]
    birthday: Optional[date]
    job: Optional[str]
    groups: List[int]
    
    
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