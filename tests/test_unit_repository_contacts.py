import unittest
from unittest.mock import MagicMock, patch

from sqlalchemy.orm import Session

from src.database.models import Contact, Group, User, Role
from src.schemas.contacts import ContactModel, ContactUpdate
from src.services.auth import Auth
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

# auth_service.r.set = MagicMock()


class TestContacts(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        # self.role = Role(name="user")
        self.user = User(id=1, role=Role(name="user"))

    @patch("Auth")
    async def test_get_contacts(self, mock):
        # user = User(role=Role("users"))
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().offset().limit().all.return_value = contacts

        # self.user.role.return_value = Role("user")
        result = await get_contacts(skip=0, limit=9, user=self.user, db=self.session)
        self.assertEqual(result, contacts)


if __name__ == '__main__':
    unittest.main()
