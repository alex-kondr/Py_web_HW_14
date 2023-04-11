from typing import List
from datetime import datetime, timedelta
import pickle

from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import UploadFile

from src.database.models import Contact, User, Group
from src.schemas.contacts import ContactBase, ContactUpdate
from src.services.upload_avatar import upload_avatar
from src.services.auth import auth_service


async def get_contacts(skip: int, limit: int, user: User, db: Session) -> List[Contact]:
    contacts = await auth_service.r.get(f"Contacts s{skip} l{limit} by {user.email}")
    if contacts:
        print("Get contacts redis")
        return pickle.loads(contacts)
    
    if user.role.name == "user":
        # print(user.role.name)
        contacts = db.query(Contact).filter(Contact.user_id == user.id).offset(skip).limit(limit).all()
    
    elif user.role.name == "admin" or user.role.name == "moderator":
        # print(user.role.name)
        contacts = db.query(Contact).offset(skip).limit(limit).all()
    
    await auth_service.r.set(f"Contacts s{skip} l{limit} by {user.email}", pickle.dumps(contacts), ex=7200)
    print("Set contacts redis")
    return contacts
    

async def get_contact(contact_id: int, user: User, db: Session) -> Contact:
    contact = await auth_service.r.get(f"Contact id:{contact_id} by {user.email}")
    if contact:
        print("Get contact redis")
        return pickle.loads(contact)
    
    if user.role.name == "user":
        contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    
    elif user.role.name == "admin" or user.role.name == "moderator":
        contact = db.query(Contact).filter(Contact.id == contact_id).first()
        
    await auth_service.r.set(f"Contact id:{contact_id} by {user.email}", pickle.dumps(contact), ex=7200)
    print("Set contacts redis")
    return contact


async def get_contact_by_fields(first_name: str,
                               last_name: str,
                               phone: str,
                               email: str,
                               days_before_birth: int,
                               user: User,
                               db: Session) -> List[Contact]:
    
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
    contact = Contact(**body.dict(), user=user)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    
    contacts_by_redis = await auth_service.r.keys("Contact*")
    await auth_service.r.delete(*contacts_by_redis)
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, user: User, db: Session):
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
        
        contacts_by_redis = await auth_service.r.keys("Contact*")
        await auth_service.r.delete(*contacts_by_redis)
    return contact


async def update_avatar(contact_id: int, file: UploadFile, user: User, db: Session):
        contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
        
        if contact:            
            contact.avatar = await upload_avatar(file, f"Contacts/{contact.first_name}_{contact.last_name}")            
            db.commit()
            
        contacts_by_redis = await auth_service.r.keys("Contact*")
        await auth_service.r.delete(*contacts_by_redis)
        return contact


# async def update_email_contact(contact_id: int, body: ContactEmailUpdate, user: User, db: Session):
#     contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    
#     if contact:
#         contact.email = body.email
#         db.commit()
        
#     return contact


async def remove_contact(contact_id: int, user: User, db: Session):
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == user.id)).first()
    
    if contact:
        db.delete(contact)
        db.commit()
        
    contacts_by_redis = await auth_service.r.keys("Contact*")
    await auth_service.r.delete(*contacts_by_redis)
    return contact