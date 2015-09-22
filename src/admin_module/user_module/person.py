# person.py


class Person:
    def __init__(self, first_name, last_name):
        """
        Initialize first_name and last_name
        :param first_name: String
        :param last_name: String
        :return:
        """
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name