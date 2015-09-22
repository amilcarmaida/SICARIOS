# customer_test.py


import unittest
from admin_module.user_module.customer import Customer


class CustomerTest(unittest.TestCase):
    
    def test_create_a_new_customer_instance(self):
        first_name = "Jon"
        last_name = "Doe"
        birth_date = "01/01/2000"
        address = "calle hachazos"
        phone = "7000000"
        email = "jon@mail.oiu"
        new_customer = Customer(first_name, last_name, birth_date, address, phone, email)
        self.assertTrue(isinstance(new_customer, Customer))
            
                
if __name__ == "__main__":
    unittest.main()