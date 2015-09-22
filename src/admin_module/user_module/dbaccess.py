__author__ = 'Amilcar Maida'

import sqlite3


class AccessDB(object):
    """Class that allows implement the login functionality"""
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        conn = sqlite3.connect('example.db')

    def search_on_db(self, user_name):
        if user_name:
            return True
