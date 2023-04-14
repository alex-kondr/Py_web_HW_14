from datetime import datetime
import unittest
from unittest.mock import MagicMock, AsyncMock
import io

from sqlalchemy.orm import Session
from fastapi import UploadFile

from src.database.models import Contact, Group, User, Role
from src.repository import contacts as repository_contacts
from src.repository.contacts import auth_service, pickle as contacts_pickle
from src.repository.contacts import (
    create_contact,
    get_contact,
    get_contact_by_fields,
    get_contacts,
    remove_contact,
    update_avatar,
    update_contact,
    update_email_contact
)
from src.schemas.contacts import ContactBase, ContactUpdate, ContactEmailUpdate


class TestContacts(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)

    async def test_get_contacts_user_without_redis(self):
        user = User(id=1, role=Role(name="user"))
        auth_service.r.get = AsyncMock(return_value=None)
        auth_service.r.set = AsyncMock()
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().offset().limit().all.return_value = contacts
        result = await get_contacts(skip=0, limit=9, user=user, db=self.session)
        self.assertEqual(result, contacts)

    async def test_get_contacts_user_without_redis_None(self):
        user = User(id=1, role=Role(name="user"))
        auth_service.r.get = AsyncMock(return_value=None)
        auth_service.r.set = AsyncMock()
        self.session.query().filter_by().offset().limit().all.return_value = None
        result = await get_contacts(skip=0, limit=9, user=user, db=self.session)
        self.assertIsNone(result)

    async def test_get_contacts_admin_without_redis(self):
        user = User(id=1, role=Role(name="admin"))
        auth_service.r.get = AsyncMock(return_value=None)
        auth_service.r.set = AsyncMock()
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().offset().limit().all.return_value = contacts
        result = await get_contacts(skip=0, limit=9, user=user, db=self.session)
        self.assertEqual(result, contacts)

    async def test_get_contacts_with_redis(self):
        user = User(id=1)
        contacts = [Contact(), Contact(), Contact()]
        auth_service.r.get = AsyncMock(return_value="contacts")
        contacts_pickle.loads = MagicMock(return_value=contacts)
        result = await get_contacts(skip=0, limit=9, user=user, db=self.session)
        self.assertEqual(result, contacts)

    async def test_get_contact_user_without_redis(self):
        user = User(id=1, role=Role(name="user"))
        auth_service.r.get = AsyncMock(return_value=None)
        auth_service.r.set = AsyncMock()
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await get_contact(contact_id=1, user=user, db=self.session)
        self.assertEqual(result, contact)

    async def test_get_contact_admin_without_redis(self):
        user = User(id=1, role=Role(name="admin"))
        auth_service.r.get = AsyncMock(return_value=None)
        auth_service.r.set = AsyncMock()
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await get_contact(contact_id=1, user=user, db=self.session)
        self.assertEqual(result, contact)

    async def test_get_contact_with_redis(self):
        user = User(id=1)
        contact = Contact()
        auth_service.r.get = AsyncMock(return_value="contacts")
        contacts_pickle.loads = MagicMock(return_value=contact)
        result = await get_contact(contact_id=1, user=user, db=self.session)
        self.assertEqual(result, contact)

    async def test_get_contact_user_without_redis_None(self):
        user = User(id=1, role=Role(name="user"))
        auth_service.r.get = AsyncMock(return_value=None)
        auth_service.r.set = AsyncMock()
        self.session.query().filter().first.return_value = None
        result = await get_contact(contact_id=1, user=user, db=self.session)
        self.assertIsNone(result)

    async def test_get_contact_by_fields_first_name(self):
        user = User(id=1)
        contact = Contact()
        self.session.query().filter().filter().all.return_value = contact
        result = await get_contact_by_fields(user=user, db=self.session, first_name="name")
        self.assertEqual(result, contact)

    async def test_get_contact_by_fields_last_name(self):
        user = User(id=1)
        contact = Contact()
        self.session.query().filter().filter().all.return_value = contact
        result = await get_contact_by_fields(user=user, db=self.session, last_name="name")
        self.assertEqual(result, contact)

    async def test_get_contact_by_fields_phone(self):
        user = User(id=1)
        contact = Contact()
        self.session.query().filter().filter().all.return_value = contact
        result = await get_contact_by_fields(user=user, db=self.session, phone="phone")
        self.assertEqual(result, contact)

    async def test_get_contact_by_fields_email(self):
        user = User(id=1)
        contact = Contact()
        self.session.query().filter().filter().all.return_value = contact
        result = await get_contact_by_fields(user=user, db=self.session, email="email")
        self.assertEqual(result, contact)

    async def test_create_contact(self):
        auth_service.r.keys = AsyncMock()
        auth_service.r.delete = AsyncMock()
        user = User(id=1)
        body = ContactBase(
            first_name="first",
            last_name="last",
            phone="+38(050)123-45-78"
        )
        result = await create_contact(body=body, user=user, db=self.session)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.phone, body.phone)
        self.assertEqual(result.user, user)
        self.assertTrue(hasattr(result, "id"))

    async def test_update_contact(self):
        auth_service.r.keys = AsyncMock()
        auth_service.r.delete = AsyncMock()
        user = User(id=1)
        contact = Contact(id=1, user=user)
        groups = [Group(name="a"), Group(name="b"), Group(name="c")]
        self.session.query().filter().all.return_value = groups
        self.session.query().filter().first.return_value = contact
        body = ContactUpdate(
            first_name="first",
            last_name="last",
            phone="+38(050)123-45-78",
            email="email@dot.com",
            birthday=datetime.now(),
            job="job",
            groups=[]
        )
        result = await update_contact(contact_id=1, body=body, user=user, db=self.session)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.phone, body.phone)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.birthday, body.birthday)
        self.assertEqual(result.job, body.job)
        self.assertEqual(result.groups, groups)
        self.assertEqual(result.user, user)
        self.assertTrue(hasattr(result, "id"))

    async def test_update_avatar(self):
        auth_service.r.keys = AsyncMock()
        auth_service.r.delete = AsyncMock()
        stream_str = io.BytesIO(b"JournalDev Python: \x00\x01")
        file = UploadFile(stream_str)
        url = "avatar"
        repository_contacts.upload_avatar = AsyncMock(return_value=url)
        user = User(id=1)
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await update_avatar(contact_id=1, file=file, user=user, db=self.session)
        self.assertEqual(result.avatar, url)

    async def test_update_email_contact(self):
        user = User(id=1)
        contact = Contact()
        body = ContactEmailUpdate(email="email@dot.com")
        self.session.query().filter().first.return_value = contact
        result = await update_email_contact(contact_id=1, body=body, user=user, db=self.session)
        self.assertEqual(result.email, body.email)

    async def test_remove_contact(self):
        auth_service.r.keys = AsyncMock()
        auth_service.r.delete = AsyncMock()
        user = User(id=1)
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await remove_contact(contact_id=1, user=user, db=self.session)
        self.assertEqual(result, contact)


if __name__ == '__main__':
    unittest.main()
