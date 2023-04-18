from typing import List, Type, Optional

from fastapi import APIRouter, HTTPException, Depends, status, UploadFile, File
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User, Contact
from src.schemas.contacts import ContactBase, ContactResponse, ContactUpdate
from src.repository import contacts as repository_contacts
from src.services.auth import auth_service

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactResponse],
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_contacts(skip: int = 0, limit: int = 9,
                        current_user: User = Depends(auth_service.get_current_user),
                        db: Session = Depends(get_db)) -> List[Contact]:
    """
    The read_contacts function returns a list of contacts.

    :param skip: int: Skip the first n contacts
    :param limit: int: Limit the number of contacts returned
    :param current_user: User: Get the current user from the token
    :param db: Session: Pass the database session to the repository layer
    :return: A list of contacts
    """
    contacts = await repository_contacts.get_contacts(skip, limit, current_user, db)
    return contacts


@router.get("/find", response_model=List[ContactResponse],
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def find_contacts_by_fields(first_name: str = None,
                                  last_name: str = None,
                                  phone: str = None,
                                  email: str = None,
                                  days_before_birth: Optional[int] = None,
                                  current_user: User = Depends(auth_service.get_current_user),
                                  db: Session = Depends(get_db)) -> List[Type[Contact]]:
    """
    The find_contacts_by_fields function is used to find contacts by first name, last name, phone number and email.
    It also allows the user to specify how many days before a contact's birthday they want to be notified.

    :param first_name: str: Specify the first name of the contact to be found
    :param last_name: str: Find the contact by last name
    :param phone: str: Search for a contact by phone number
    :param email: str: Find a contact by email
    :param days_before_birth: int: Find contacts that have their birthdays in the next 7 days
    :param current_user: User: Get the current user
    :param db: Session: Pass the database session to the repository layer
    :return: A list of contacts
    """
    contact = await repository_contacts.get_contact_by_fields(current_user,
                                                              db,
                                                              first_name,
                                                              last_name,
                                                              phone,
                                                              email,
                                                              days_before_birth)

    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.get("/{contact_id}", response_model=ContactResponse,
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_contact(contact_id: int,
                       current_user: User = Depends(auth_service.get_current_user),
                       db: Session = Depends(get_db)) -> Contact:
    """
    The read_contact function is used to retrieve a single contact from the database.
    It takes in an integer representing the ID of the contact, and returns a Contact object.

    :param contact_id: int: Specify the contact id
    :param current_user: User: Get the current user from the database
    :param db: Session: Pass the database session to the repository layer
    :return: The contact object
    """
    contact = await repository_contacts.get_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED,
             description="No more than 10 requests per minute",
             dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def create_contact(body: ContactBase,
                         current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)) -> Contact:
    """
    The create_contact function creates a new contact in the database.

    :param body: ContactBase: Get the data from the request body
    :param current_user: User: Get the user that is currently logged-in
    :param db: Session: Pass the database session to the repository
    :return: A contact object
    """
    return await repository_contacts.create_contact(body, current_user, db)


@router.put("/{contact_id}", response_model=ContactResponse,
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def update_contact(body: ContactUpdate, contact_id: int,
                         current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)) -> Contact:
    """
    The update_contact function updates a contact in the database.
        The function takes an id of the contact to update, and a ContactUpdate object containing
        all fields that should be updated.

    :param body: ContactUpdate: Get the data from the request body
    :param contact_id: int: Specify the id of the contact to be deleted
    :param current_user: User: Get the current user from the database
    :param db: Session: Pass the database session to the repository
    :return: A contact object
    """
    contact = await repository_contacts.update_contact(contact_id, body, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.patch("/{contact_id}", response_model=ContactResponse,
              description="No more than 10 requests per minute",
              dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def update_avatar(contact_id: int, file: UploadFile = File(),
                        current_user: User = Depends(auth_service.get_current_user),
                        db: Session = Depends(get_db)) -> Contact:
    """
    The update_avatar function updates the avatar of a contact.
        The function takes in an integer representing the id of the contact to be updated,
        and a file object containing information about the new avatar image.

    :param contact_id: int: Identify the contact to be updated
    :param file: UploadFile: Upload the file to the server
    :param current_user: User: Get the current user
    :param db: Session: Pass the database session to the repository layer
    :return: A contact object
    """
    contact = await repository_contacts.update_avatar(contact_id, file, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    return contact


@router.delete("/{contact_id}", response_model=ContactResponse, status_code=status.HTTP_202_ACCEPTED,
               description="No more than 10 requests per minute",
               dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def remove_contact(contact_id: int,
                         current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)) -> Contact:
    """
    The remove_contact function removes a contact from the database.

    :param contact_id: int: Specify the contact to be deleted
    :param current_user: User: Get the current user from the database
    :param db: Session: Pass the database session to the repository layer
    :return: The contact that was deleted
    """
    contact = await repository_contacts.remove_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact
