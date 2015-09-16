# customer.p


from person import Person


class Customer(Person):
    """
    customer constructor
    """
    def __init__(self, first_name, last_name, birth_date, address, phone, email):
        Person.__init__(self, first_name, last_name, birth_date)
        self._address = address
        self._phone = phone
        self._email = email
        
    def get_birth_date(self):
        return self._birth_date
    
    def get_address(self):
        return self._address
    
    def get_phone_number(self):
        return self._phone
    
    def get_email(self):
        return self._email


    
    

