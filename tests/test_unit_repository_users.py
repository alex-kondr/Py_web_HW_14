import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from tests.conftest import session
from src.database.models import User, Role
from src.schemas.users import UserModel
from src.repository.users import (
    get_user_by_email,
    update_user,
    update_avatar,
    create_user,
    update_token,
    confirmed_email,
    save_new_password
)


class TestContacts(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = session
        # self.user = User(id=1)
        # self.user.role = Role("user")

    # async def test_create_user(self):
    #     body = UserModel(
    #         password="123456",
    #         username="qwerty",
    #         phone="+38-012-345-45-78"
    #     )
    #
    #     result = await create_user(body=body, db=self.session)
    #     print(result)

        # user = User(role=Role("users"))
        # contacts = [Contact(), Contact(), Contact()]
        # self.session.query().filter_by().offset().limit().all.return_value = contacts
        #
        # self.user.role.return_value = Role("user")
        # result = await get_contacts(skip=0, limit=9, user=self.user, db=self.session)
        # self.assertEqual(result, contacts)


if __name__ == '__main__':
    unittest.main()
