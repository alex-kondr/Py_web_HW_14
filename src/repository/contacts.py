from typing import List, Type, Optional
from datetime import datetime, timedelta
import pickle

from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import UploadFile

from src.database.models import Contact, User, Group
from src.schemas.contacts import ContactBase, ContactUpdate, ContactEmailUpdate
from src.services.upload_avatar import upload_avatar
from src.services.auth import auth_service


async def get_contacts(skip: int, limit: int, user: User, db: Session) -> List[Contact]:
    """
    The get_contacts function is used to retrieve a list of contacts from the database. The function takes in three
    parameters: skip, limit, and user. The skip parameter is an integer that specifies how many contacts should be
    skipped before retrieving the next set of contacts. The limit parameter is an integer that specifies how many
    contacts should be retrieved at once (the maximum number). Finally, the user parameter represents a User object
    which contains information about who made this request for contact data.

    :param skip: int: Skip the first n contacts in the database
    :param limit: int: Limit the number of contacts returned
    :param user: User: Check the role of the user making the request
    :param db: Session: Access the database
    :return: A list of contacts, which is a list of dictionaries
    """
    contacts = await auth_service.r.get(f"Contacts by {user.email} s{skip} l{limit}")
    if contacts:
        return pickle.loads(contacts)

    if user.role.name == "user":
        contacts = db.query(Contact).filter_by(user_id=user.id).offset(skip).limit(limit).all()

    elif user.role.name == "admin" or user.role.name == "moderator":
        contacts = db.query(Contact).offset(skip).limit(limit).all()

    await auth_service.r.set(f"Contacts by {user.email} s{skip} l{limit}", pickle.dumps(contacts), ex=7200)
    return contacts


async def get_contact(contact_id: int, user: User, db: Session) -> Contact:
    """
    The get_contact function is used to retrieve a contact from the database.
        It takes in three parameters:
            - contact_id: The id of the contact you want to retrieve.
            - user: The user who is requesting this information (used for authorization).
            - db: A connection to the database that will be used for querying.

    :param contact_id: int: Get the contact from the database
    :param user: User: Check if the user is an admin or moderator, and can therefore view all contacts
    :param db: Session: Access the database
    :return: A contact object for a given id
    """
    contact = await auth_service.r.get(f"Contact id:{contact_id} by {user.email}")
    if contact:
        return pickle.loads(contact)

    if user.role.name == "user":
        contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()

    elif user.role.name == "admin" or user.role.name == "moderator":
        contact = db.query(Contact).filter(Contact.id == contact_id).first()

    await auth_service.r.set(f"Contact id:{contact_id} by {user.email}", pickle.dumps(contact), ex=7200)
    return contact


async def get_contact_by_fields(user: User,
                                db: Session,
                                first_name: str = None,
                                last_name: str = None,
                                phone: str = None,
                                email: str = None,
                                days_before_birth: int = None) -> List[Type[Contact]]:

    """
    The get_contact_by_fields function is used to search for contacts by any of the following fields:
    first_name, last_name, phone, email and days_before_birth. The function returns a list of all contacts that match
    the given criteria.

    :param user: User: Ensure that the user is logged in and has access to the database
    :param db: Session: Pass the database session to the function
    :param first_name: str: Filter the contacts by first name
    :param last_name: str: Filter the contacts by last name
    :param phone: str: Filter the contacts by phone number
    :param email: str: Filter the contacts by email
    :param days_before_birth: int: Filter the contacts by their birthday
    :return: All contacts that match the specified fields
    """
    contact = db.query(Contact)

    if first_name:
        contact = contact.filter(and_(Contact.first_name == first_name, Contact.user_id == user.id))

    if last_name:
        contact = contact.filter(and_(Contact.last_name == last_name, Contact.user_id == user.id))

    if phone:
        contact = contact.filter(and_(Contact.phone == phone, Contact.user_id == user.id))

    if email:
        contact = contact.filter(and_(Contact.email == email, Contact.user_id == user.id))

    start_date = datetime.now()
    end_date = start_date + timedelta(days=days_before_birth)
    contact = contact.filter(and_(Contact.birthday.between(start_date, end_date), Contact.user_id == user.id))

    return contact.all()


async def create_contact(body: ContactBase, user: User, db: Session) -> Contact:
    """
    The create_contact function creates a new contact in the database.

    :param body: ContactBase: Get the data from the request body
    :param user: User: Get the user id from the jwt token
    :param db: Session: Access the database
    :return: A contact object
    """
    contact = Contact(**body.dict(), user=user)
    db.add(contact)
    db.commit()
    db.refresh(contact)

    contacts_by_redis = await auth_service.r.keys(f"Contact id:{contact.id}*")
    if contacts_by_redis:
        await auth_service.r.delete(*contacts_by_redis)
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, user: User, db: Session) -> Optional[Contact]:
    """
    The update_contact function updates a contact in the database. Args: contact_id (int): The id of the contact to
    update. body (ContactUpdate): The updated information for the specified user's contact. user (User): The current
    logged-in user, used to verify that they are updating their own data and not someone else's.

    :param contact_id: int: Identify the contact to be deleted
    :param body: ContactUpdate: Pass the updated contact information to the function
    :param user: User: Get the user id from the jwt token
    :param db: Session: Access the database
    :return: The updated contact
    """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()

    if contact:
        groups = db.query(Group).filter(and_(Group.id.in_(body.groups), Group.user_id == user.id)).all()

        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.phone = body.phone
        contact.email = body.email
        contact.birthday = body.birthday
        contact.job = body.job
        contact.groups = groups

        db.commit()

        contacts_by_redis = await auth_service.r.keys(f"Contact id:{contact.id}*")
        if contacts_by_redis:
            await auth_service.r.delete(*contacts_by_redis)
    return contact


async def update_avatar(contact_id: int, file: UploadFile, user: User, db: Session) -> Optional[Contact]:
    """
    The update_avatar function updates the avatar of a contact. Args: contact_id (int): The id of the contact to
    update. file (UploadFile): The new avatar image for the user. user (User): The current logged-in user,
    used to verify that they are updating their own account and not someone else's.

    :param contact_id: int: Find the contact in the database
    :param file: UploadFile: Upload the avatar to the database
    :param user: User: Check if the user is authorized to update the contact
    :param db: Session: Access the database
    :return: The updated contact
    """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()

    if contact:
        contact.avatar = await upload_avatar(file, f"Contacts/{contact.first_name}_{contact.last_name}")
        db.commit()

    contacts_by_redis = await auth_service.r.keys(f"Contact id:{contact.id}*")
    if contacts_by_redis:
        await auth_service.r.delete(*contacts_by_redis)
    return contact


async def update_email_contact(contact_id: int, body: ContactEmailUpdate, user: User, db: Session) -> Optional[Contact]:
    """
    The update_email_contact function updates the email of a contact in the database.

    :param contact_id: int: Identify the contact to be updated
    :param body: ContactEmailUpdate: Pass the new email address to be updated
    :param user: User: Check if the user is authorized to update a contact
    :param db: Session: Pass in the database session
    :return: The updated contact
    """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()

    if contact:
        contact.email = body.email
        db.commit()

    return contact


async def remove_contact(contact_id: int, user: User, db: Session) -> Optional[Contact]:
    """
    The remove_contact function removes a contact from the database.
        Args:
            contact_id (int): The id of the contact to be removed.
            user (User): The user who is removing the contact.
            db (Session): A connection to our database, used for querying and deleting contacts.

    :param contact_id: int: Identify the contact to be removed
    :param user: User: Check if the user is authorized to delete a contact
    :param db: Session: Access the database
    :return: The contact that was removed
    """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()

    if contact:
        db.delete(contact)
        db.commit()

    contacts_by_redis = await auth_service.r.keys(f"Contact id:{contact.id}*")
    if contacts_by_redis:
        await auth_service.r.delete(*contacts_by_redis)
    return contact
