import unittest
from generalreview import *
class TestGeneralReviews(unittest.TestCase):
    def setUp(self):
        self.customer1 = GeneralReview("Patrick", "8192104615", "patrick@gmail.com", "5", "4", "5")
        self.customer2 = GeneralReview("Alyssa", "7102487366", "alyssa@gmail.com", "4", "5", "3")
        self.customer3 = GeneralReview("Jose", "7328449299", "jose@gmail.com", "4", "4", "4")
        self.customer4 = GeneralReview("Karen", "8773934443", "karen@gmail.com", "1", "1", "1")
        self.customer5 = GeneralReview("Pat", "8129104165", "pat@gmail.com", "5", "3", "5")
        self.customer6 = GeneralReview("Rick", "1892401651", "rick@gmail.com", "4", "4", "3")
    
    def test_from_form(self):
        
        self.assertRaises(TypeError, self.customer6.from_form, {'name':55, 'phoneNumber':"800405212", 'email':"jonathan@techexchange.in", 'cleaninessGrade':5, 'serverGrade':5, 'treatmentGrade':5})
        self.assertRaises(TypeError, self.customer6.from_form, {'name':"Jonathan", 'phoneNumber':800405212, 'email':"jonathan@techexchange.in", 'cleaninessGrade':5, 'serverGrade':5, 'treatmentGrade':5})
        self.assertRaises(TypeError, self.customer6.from_form, {'name':"Jonathan", 'phoneNumber':"800405212", 'email':"jonathan@techexchange.in", 'cleaninessGrade':"5", 'serverGrade':5, 'treatmentGrade':5})
        self.assertRaises(TypeError, self.customer6.from_form, {'name':"Jonathan", 'phoneNumber':"800405212", 'email':"jonathan@techexchange.in", 'cleaninessGrade':5, 'serverGrade':"5", 'treatmentGrade':5})
        self.assertRaises(TypeError, self.customer6.from_form, {'name':"Jonathan", 'phoneNumber':"800405212", 'email':"jonathan@techexchange.in", 'cleaninessGrade':5, 'serverGrade':5, 'treatmentGrade':"5"})
        self.assertRaises(TypeError, self.customer6.from_form, {'name':"Pat", 'phoneNumber':"800405212", 'email':"pat@gmail.com", 'cleaninessGrade':"5", 'serverGrade':"5", 'treatmentGrade':"5"})
        self.assertRaises(TypeError, self.customer6.from_form, {'name':"Pat", 'phoneNumber':"80040521202", 'email':"pat@gmail.com", 'cleaninessGrade':"5", 'serverGrade':"5", 'treatmentGrade':"5"})
    
    def test_from_document(self):
        self.assertRaises(ValueError, self.customer6.from_document, None)

    def test_to_document(self):
        self.assertEqual(self.customer2.to_document(), {"name":"Alyssa", "number": "7102487366", "email": "alyssa@gmail.com", "cleaniness grade": "4", "service grade": "5", "treatment grade":"3"})
        self.assertEqual(self.customer1.to_document(), {"name":"Patrick", "number": "8192104615", "email": "patrick@gmail.com", "cleaniness grade": "5", "service grade": "4", "treatment grade":"5"})
        self.assertEqual(self.customer3.to_document(), {"name":"Jose", "number": "7328449299", "email": "jose@gmail.com", "cleaniness grade": "4", "service grade": "4", "treatment grade":"4"})
if __name__ == "__main__":
    unittest.main()