# login.py


class Login(object):
    """
    Class that allows implement the login functionality
    """
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def login_init(self, user_name, password):
        if user_name == user_name and password == password:
            return True
        else:
            print("The user or password are invalid")