import unittest

from beanie import init_beanie
from mongomock_motor import AsyncMongoMockClient
from jsecurity_persistence.models.user import User


class UserTest(unittest.IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = AsyncMongoMockClient()

    async def test_user_insert_one(self):
        await init_beanie(database=self.client.Dev, document_models=[User])
        await User(email='test@example.org', password='password').insert()
        user = await User.find_one(User.email == 'test@example.org')
        self.assertIsNotNone(user)
        self.assertEqual(user.password, 'password')
