import unittest
from customer_reviews import *

class Test_Customer_Reviews(unittest.TestCase):

    def setUp(self):
        
        #creating instances of class Review
        self.customer1 = Reviews()
        self.customer2 = Reviews()
        self.customer3 = Reviews()
        self.customer4 = Reviews()
        self.customer5= Reviews()

        #Adding information to certain instances of class Review
        self.customer1.general_reviews("Patrick", "8192104615", "patrick@gmail.com", 5, 4, 5)
        self.customer2.general_reviews("Alyssa", "7102487366", "alyssa@gmail.com", 4, 5, 3)
        self.customer3.general_reviews("Jose", "7328449299", "jose@gmail.com", 4, 4, 4)
        self.customer4.general_reviews("Karen", "8773934443", "karen@gmail.com", 1, 1, 1)

        self.customer1.items_review("Patrick", "8192104615", "patrick@gmail.com", 5, 4, 5)
        self.customer2.items_review("Alyssa", "7102487366", "alyssa@gmail.com", 4, 5, 3)
        self.customer3.items_review("Jose", "7328449299", "jose@gmail.com", 4, 4, 4)
        self.customer4.items_review("Karen", "8773934443", "karen@gmail.com", 1, 1, 1)

    def test_general_review(self):     
        
        #Tests to ensure correct type errors are raised when wrong types are passed in
        self.assertRaises(TypeError, self.customer5.general_reviews, 55, "800405212", "jonathan@techexchange.in", 5, 5, 5)
        self.assertRaises(TypeError, self.customer5.general_reviews,"Jonathan", 800405212, "jonathan@techexchange.in", 5, 5, 5)
        self.assertRaises(TypeError, self.customer5.general_reviews,"Jonathan", "800405212", "jonathan@techexchange.in", "5", 5, 5)
        self.assertRaises(TypeError, self.customer5.general_reviews,"Jonathan", "800405212", "jonathan@techexchange.in", 5, "5", 5)
        self.assertRaises(TypeError, self.customer5.general_reviews,"Jonathan", "800405212", "jonathan@techexchange.in", 5, 5, "5")
        #Tests to ensure that value errors are raised when incorrect values are passed in 
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "8004052124", "jonathan@techexchange.in", 0, 5, 5)
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "8004052123", "jonathan@techexchange.in", 6, 1, 1)
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "8004052125", "jonathan@techexchange.in", 5, -2, 5)
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "8004052123", "jonathan@techexchange.in", 4, 9, 5)
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "8004052128", "jonathan@techexchange.in", 5, 5, -1)
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "8004052127", "jonathan@techexchange.in", 2, 2, 100)
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "88004052127", "jonathan@techexchange.in", 4, 4, 5)
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "a800405212", "jonathan@techexchange.in", 4, 4, 5)
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "280-040-5212", "jonathan@techexchange.in", 4, 4, 5)
        self.assertRaises(ValueError, self.customer5.general_reviews,"Jonathan", "4052127", "jonathan@techexchange.in", 4, 4, 5)

        self.assertEqual(self.customer5.general_reviews(None, None, None, 5, 5, 5),"Invalid Review!/n Name and contact info must be written.")

    def test_get_general_reviews(self):

        #Tests to verify that created objects are present in the class variables
        self.assertEqual(self.customer2.get_general_review("Alyssa"), {"name":"Alyssa", "number": "7102487366", "email": "alyssa@gmail.com", "cleaniness grade": 4, "service grade": 5, "treatment grade":3})
        self.assertEqual(self.customer1.get_general_review("Patrick"), {"name":"Patrick", "number": "8192104615", "email": "patrick@gmail.com", "cleaniness grade": 5, "service grade": 4, "treatment grade":5})
        self.assertEqual(self.customer3.get_general_review("Jose"), {"name":"Jose", "number": "7328449299", "email": "jose@gmail.com", "cleaniness grade": 4, "service grade": 4, "treatment grade":4})
        #Tests to check if values that are not supposed to be present produce the output string
        self.assertEqual(self.customer2.get_general_review("alyssa"), "Customer not found!")
        self.assertEqual(self.customer5.get_general_review("Mae"), "Customer not found!")
        self.assertEqual(self.customer3.get_general_review(15), "Customer not found!")
        self.assertEqual(self.customer3.get_general_review(True), "Customer not found!")

        
    def test_items_review(self):

        #Tests to ensure correct type errors are raised when wrong types are passed in
        self.assertRaises(TypeError, self.customer5.items_review, 55, "800405212", "jonathan@techexchange.in", 5, 5, 5)
        self.assertRaises(TypeError, self.customer5.items_review,"Jonathan", 800405212, "jonathan@techexchange.in", 5, 5, 5)
        self.assertRaises(TypeError, self.customer5.items_review,"Jonathan", "800405212", "jonathan@techexchange.in", "5", 5, 5)
        self.assertRaises(TypeError, self.customer5.items_review,"Jonathan", "800405212", "jonathan@techexchange.in", 5, "5", 5)
        self.assertRaises(TypeError, self.customer5.items_review,"Jonathan", "800405212", "jonathan@techexchange.in", 5, 5, "5")
        #Tests to ensure that value errors are raised when incorrect values are passed in 
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "8004052124", "jonathan@techexchange.in", 0, 5, 5)
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "8004052123", "jonathan@techexchange.in", 6, 1, 1)
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "8004052125", "jonathan@techexchange.in", 5, -2, 5)
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "8004052123", "jonathan@techexchange.in", 4, 9, 5)
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "8004052128", "jonathan@techexchange.in", 5, 5, -1)
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "8004052127", "jonathan@techexchange.in", 2, 2, 100)
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "88004052127", "jonathan@techexchange.in", 4, 4, 5)
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "a800405212", "jonathan@techexchange.in", 4, 4, 5)
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "800-405-2127", "jonathan@techexchange.in", 4, 4, 5)
        self.assertRaises(ValueError, self.customer5.items_review,"Jonathan", "4052127", "jonathan@techexchange.in", 4, 4, 5)


    def test_get_items_review(self):
        
        #Tests to verify that created objects are present in the class variables
        self.assertEqual(self.customer2.get_items_review("Alyssa"), {"name":"Alyssa", "number": "7102487366", "email": "alyssa@gmail.com", "cleaniness grade": 4, "service grade": 5, "treatment grade":3})
        self.assertEqual(self.customer1.get_items_review("Patrick"), {"name":"Patrick", "number": "8192104615", "email": "patrick@gmail.com", "cleaniness grade": 5, "service grade": 4, "treatment grade":5})
        self.assertEqual(self.customer3.get_items_review("Jose"), {"name":"Jose", "number": "7328449299", "email": "jose@gmail.com", "cleaniness grade": 4, "service grade": 4, "treatment grade":4})
        #Tests to check if values that are not supposed to be present produce the output string
        self.assertEqual(self.customer2.get_items_review("alyssa"), "Customer not found!")
        self.assertEqual(self.customer5.get_items_review("Mae"), "Customer not found!")
        self.assertEqual(self.customer3.get_items_review(105), "Customer not found!")
        self.assertEqual(self.customer3.get_items_review(False), "Customer not found!")        


if __name__ == "__main__":
    unittest.main()