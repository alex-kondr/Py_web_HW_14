from datetime import datetime
import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas.users import UserBase, UserUpdate
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
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    async def test_get_user_by_email(self):
        self.session.query().filter().first.return_value = self.user
        result = await get_user_by_email(email="email", db=self.session)
        self.assertEqual(result, self.user)

    async def test_update_user(self):
        body = UserUpdate(
            first_name="first",
            last_name="last",
            username="username",
            birthday=datetime.now(),
            job="job",
            phone="+38(050)123-45-78"
        )
        result = await update_user(body=body, user=self.user, db=self.session)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.birthday, body.birthday)
        self.assertEqual(result.job, body.job)
        self.assertEqual(result.phone, body.phone)

    async def test_update_avatar(self):
        self.session.query().filter().first.return_value = self.user
        url = "url"
        result = await update_avatar(email="email@dot.com", url=url, db=self.session)
        self.assertEqual(result.avatar, url)

    async def test_create_user(self):
        body = UserBase(
            password="123456",
            username="qwerty",
            phone="+38-012-345-45-78",
            email="emai@dot.com"
        )
        result = await create_user(body=body, db=self.session)
        self.assertEqual(result.password, body.password)
        self.assertEqual(result.username, body.username)
        self.assertEqual(result.phone, body.phone)
        self.assertEqual(result.email, body.email)
        self.assertIsNone(result.job)
        self.assertIsNone(result.birthday)
        self.assertTrue(hasattr(result, "id"))

    async def test_update_token(self):
        refresh_token = "token"
        result = await update_token(user=self.user, token=refresh_token, db=self.session)
        self.assertIsNone(result)
        self.assertEqual(self.user.refresh_token, refresh_token)

    async def test_confirmed_email(self):
        result = await confirmed_email(user=self.user, db=self.session)
        self.assertIsNone(result)
        self.assertTrue(self.user.confirmed)

    async def test_save_new_password(self):
        password = "password"
        result = await save_new_password(user=self.user, password_hash=password, db=self.session)
        self.assertIsNone(result)
        self.assertEqual(self.user.password, password)


if __name__ == '__main__':
    unittest.main()
