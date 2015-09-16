# This the user class


from person import Person
from sellrent import SellRent
from get_access import Login
from buildreport import BuildReport


class User(Person):
    """Class constructor that allows define the user and their attributes"""
    def __init__(self, first_name, last_name, role, user_name, password, birthdate):
        self.role = role
        self.password = password
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birthdate
        Person.__init__(self, first_name, last_name, birthdate)

    def sell_movies(self, user_name, password):
        """Method to sell movies"""
        if Login.login_init(user_name, password):
            if self.role == 'Administrator' or self.role == 'Employee':
                SellRent.sell_a_movie()
                return True
            else:
                print "You must be the Administrator or Employee to be able to sell movies"
        else:
            print "User or password incorrect, please try with valid credentials"

    def rent_movies(self, user_name, password):
        """Method to rent movies"""
        if Login.login_init(user_name, password):
            if self.role == 'Administrator' or self.role == 'Employee':
                SellRent.rent_a_movie()
                return True
            else:
                print "You must be the Administrator or Employee to be able to rent movies"
        else:
            print "User or password incorrect, please try with valid credentials"

    def return_movie(self, user_name, password):
        """Method to return movies"""
        if Login.login_init(user_name, password):
            if self.role == 'Administrator' or self.role == 'Employee':
                SellRent.return_a_movie()
                return True
            else:
                print "You must be the Administrator or Employee to be able to return movies"
        else:
            print "User or password incorrect, please try with valid credentials"

    def generate_report(self, user_name, password):
        """Method to generate reports"""
        if Login.login_init(user_name, password):
            if self.role == 'Administrator' or self.role == 'Employee':
                BuildReport.build_report()
            else:
                print "You must be the Administrator or Employee to be able to generate reports"
        else:
            print "User or password incorrect, please try with valid credentials"


