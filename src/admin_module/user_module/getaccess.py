__author__ = 'Amilcar Maida'

from src.admin_module.user_module.user import User


class GetAccess(User):
    """Class that allows implement the login functionality"""
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def login_init(self, user_name):

        if User.search_user(user_name):
            return True
        else:
            print "The user or password is invalid"
