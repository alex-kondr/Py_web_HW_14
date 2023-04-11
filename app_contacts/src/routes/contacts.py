from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, UploadFile, File
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User
from src.schemas.contacts import ContactBase, ContactModel, ContactResponse, ContactUpdate, ContactEmailUpdate
from src.repository import contacts as repository_contacts
from src.services.auth import auth_service


router = APIRouter(prefix="/contacts", tags=["contacs"])


@router.get("/", response_model=List[ContactResponse],
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_contacts(skip: int = 0, limit: int = 10,
                        current_user: User = Depends(auth_service.get_current_user),
                        db: Session = Depends(get_db)):
    
    contacts = await repository_contacts.get_contacts(skip, limit, current_user, db)
    return contacts


@router.get("/find", response_model=List[ContactResponse],
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def find_contacts_by_fields(first_name: str = None,
                                 last_name: str = None,
                                 phone: str = None,
                                 email: str = None,
                                 days_before_birth: int = 7,
                                 current_user: User = Depends(auth_service.get_current_user),
                                 db: Session = Depends(get_db)):
    
    contact = await repository_contacts.get_contact_by_fields(first_name,
                                                             last_name,
                                                             phone,
                                                             email,
                                                             days_before_birth,
                                                             current_user,
                                                             db)
    
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.get("/{contact_id}", response_model=ContactResponse,
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_contact(contact_id: int,
                       current_user: User = Depends(auth_service.get_current_user),
                       db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED,
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def create_contact(body: ContactBase,
                         current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)):
    
    return await repository_contacts.create_contact(body, current_user, db)


@router.put("/{contact_id}", response_model=ContactResponse,
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def update_contact(body: ContactUpdate, contact_id: int,
                         current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)):
    
    contact = await repository_contacts.update_contact(contact_id, body, current_user, db)    
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.patch("/{contact_id}", response_model=ContactResponse,
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def update_avatar(contact_id: int, file: UploadFile = File(), 
                               current_user: User = Depends(auth_service.get_current_user),
                               db: Session = Depends(get_db)):
    
    contact = await repository_contacts.update_avatar(contact_id, file, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse, status_code=status.HTTP_202_ACCEPTED,
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def remove_contact(contact_id: int,
                         current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)):
    
    contact = await repository_contacts.remove_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact
