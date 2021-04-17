import unittest

from аuthorization import UserToken
from exceptions import *

class TestUserToken(unittest.TestCase):

    def setUp(self) -> None:
        self.user = UserToken()

    def test_register(self):
        with self.assertRaises(ErrorPassword):
            self.user.register('Igor', 'igor@gmail.com', 'Zaqwert')
            self.user.register('Igor', 'igor@gmail.com', 'Zaqwertyzaqwerty123')
            self.user.register('Igor', 'igor@gmail.com', '123456789')
            self.user.register('Igor', 'igor@gmail.com', 'zaqwerty123')
        with self.assertRaises(ErrorName):
            self.user.register('Igor', 'igor@gmail.com', 'Zaqwerty123')
            self.user.register('Ivanovivanivanovich', 'igor@gmail.com', 'Zaqwerty123')
        with self.assertRaises(ErrorName2):
            self.user.register('Igor/)(', 'igor@gmail.com', 'zaqwerty123')
            self.user.register(')(atabI4', 'igor@gmail.com', 'Zaqwerty123')
        with self.assertRaises(ErrorEmail2):
            self.user.register('Igor', 'igorgmail.com', 'Zaqwerty123')
            self.user.register('Igor', 'igor@@gmail..com', 'Zaqwerty123')
            self.user.register('Igor', 'igor@)))(((][.com', 'Zaqwerty123')
        with self.assertRaises(ErrorEmail):
            self.user.register('Igor', '@gmail.com', 'Zaqwerty123')
            self.user.register('Igor', '@.com', 'Zaqwerty123')
        self.assertEqual(self.user.register('Yuriy', 'yuriy@gmail.com', 'Zaqwerty123'), 200)

    def test_login_in(self):
        with self.assertRaises(ErrorLoginPassword):
            self.user.login_in('yr@gmail.com', 'Zaqwerty')
        self.user.login_in('yuriy@gmail.com', 'Zaqwerty123')

    def tearDown(self) -> None:
        print('Stop')


if __name__ == '__main__':
    unittest.main(verbosity=2)
