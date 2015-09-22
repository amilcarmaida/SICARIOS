__author__ = 'Amilcar Maida'


import unittest
from src.admin_module.user_module.user import User


class UserTest(unittest.TestCase):

    def test_create_a_new_user_instance(self):
        user_test = User("Jhonny", "Page", "Employee", "Jonny", "Control123")
        self.assertTrue(isinstance(user_test, User))

    def test_validate_login_access_True(self):
        user_test = User("Jhonny", "Page", "Employee", "Jonny", "Control123")
        user_name = 'Pedro'
        password = 'Control234'
        self.assertTrue(user_test.login_user(user_name, password))


if __name__ == "__main__":
    unittest.main()
