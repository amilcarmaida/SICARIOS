# unit test class


import unittest
from admin_module.user_module.user import User


class UserTest(unittest.TestCase):

    def test_create_a_new_user_instance(self):
        user_test = User("Jhonny", "Page", "Employee", "Jonny", "Control123", "01/01/1985")
        self.assertTrue(isinstance(user_test, User))


if __name__ == "__main__":
    unittest.main()