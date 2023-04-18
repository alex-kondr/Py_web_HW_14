import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from src.database.models import Group, User
from src.schemas.groups import GroupModel, GroupUpdate
from src.repository.groups import (
    create_group,
    get_group,
    get_groups,
    remove_group,
    update_group
)


class TestGroups(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    async def test_get_groups(self):
        groups = [Group(), Group(), Group()]
        self.session.query().offset().limit().all.return_value = groups
        result = await get_groups(skip=0, limit=9, db=self.session)
        self.assertEqual(result, groups)

    async def test_get_group(self):
        group = Group()
        self.session.query().filter().first.return_value = group
        result = await get_group(group_id=1, db=self.session)
        self.assertEqual(result, group)

    async def test_get_group_not_found(self):
        self.session.query().filter().first.return_value = None
        result = await get_group(group_id=1, db=self.session)
        self.assertIsNone(result)

    async def test_create_group(self):
        body = GroupModel(name="Family")
        result = await create_group(body=body, user=self.user, db=self.session)
        self.assertEqual(result.name, body.name)
        self.assertTrue(hasattr(result, "id"))

    async def test_update_group(self):
        body = GroupUpdate(name="Family")
        result = await update_group(group_id=1, body=body, user=self.user, db=self.session)
        self.assertEqual(result.name, body.name)
        self.assertTrue(hasattr(result, "id"))

    async def test_remove_group(self):
        group = Group()
        self.session.query().filter().first.return_value = group
        result = await remove_group(group_id=1, user=self.user, db=self.session)
        self.assertEqual(result, group)
