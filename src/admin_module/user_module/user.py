__author__ = 'Amilcar Maida'


from src.admin_module.user_module.person import Person
from src.admin_module.user_module.sellrent import SellRent
from src.admin_module.user_module.getaccess import GetAccess
from src.admin_module.user_module.buildreport import BuildReport
from src.admin_module.user_module.dbaccess import AccessDB
from src.admin_module.user_module.movie import Movie


class User(Person):
    """
    User class allows rent, sell and generate reports about movies available
     :method rent_movie: define the functionality to rent movies
     :method sell_movie: define the functionality to sell movies
     :method generate_report: define the functionality to generate reports
     :method return_movie: define the functionality to return movies
     :method login_user: define the functionality to get access to rent and sell
    """
    def __init__(self, first_name, last_name, role, user_name, password):
        """
        Initialize User class
        :param first_name: String
        :param last_name: String
        :param role: String
        :param user_name: String
        :param password: String
        """
        self.role = role
        self.password = password
        self.user_name = user_name
        self.in_use = False
        self.first_name = first_name
        self.last_name = last_name
        Person.__init__(self, first_name, last_name)

    def login_user(self, user_name, password):
        """
        Method to access to the system
        """
        user_name = user_name
        password = password
        get_access = GetAccess(user_name, password)
        if get_access.login_init(user_name, password):
            self.in_use = True
            return True
        else:
            return False

    def search_user(self, user_name):
        """
        Method that returns True if user exists
        """
        if search_on_db(user_name):
            print "The user is registered"
            return True
        else:
            print "The user does not exist"
            return False

    def sell_movie(self, movie_code):
        """
        Method to sell movies
        """

        if User.login_user():
            if self.role == 'Administrator' or self.role == 'Employee':
                SellRent.sell_a_movie(movie_code)
                return True
            else:
                print "You must be the Administrator or Employee to be able to sell movies"
        else:
            print "User or password incorrect, please try with valid credentials"

    def rent_movie(self, movie_code):
        """
        Method to rent movies
        """

        if User.login_user():
            if self.role == 'Administrator' or self.role == 'Employee':
                SellRent.rent_a_movie(movie_code)
                return True
            else:
                print "You must be the Administrator or Employee to be able to rent movies"
        else:
            print "User or password incorrect, please try with valid credentials"

    def return_movie(self, movie_code):
        """
        Method to return movies
        """

        if User.login_user():
            if self.role == 'Administrator' or self.role == 'Employee':
                SellRent.return_a_movie(movie_code)
                return True
            else:
                print "You must be the Administrator or Employee to be able to return movies"
        else:
            print "User or password incorrect, please try with valid credentials"

    def generate_report(self):
        """
        Method to generate reports
        """

        if User.login_user():
            if self.role == 'Administrator' or self.role == 'Employee':
                BuildReport.build_report()
            else:
                print "You must be the Administrator or Employee to be able to generate reports"
        else:
            print "User or password incorrect, please try with valid credentials"


