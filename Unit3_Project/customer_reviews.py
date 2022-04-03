import pymongo
import os

client = pymongo.MongoClient("mongodb+srv://admin:"+ os.environ.get('PASSWORD') +"@cluster0.wv93i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.myFirstDatabase
general_reviewsDB = db.general_reviews

class Reviews:
    """
    Reviews class Attributes:
    general_reviews_list -> a list which stores all the general reviews left by customers which the employees use to access
    a particluar customers review.
    items_reviews_list -> a list which stores all the item reviews left by customers which the employees use to access
    what customers think of our products.
    """
    general_reviews_list = []
    items_reviews_list =[]
    def __init__(self):
        """
        Reviews Constructor:
        self.general_reviews_dict: A dictionary which stores each customer's general review.
        self.items_reviews_dict: A dictionary which stores each customer's items review.
        """
        self.general_reviews_dict = {}
        self.items_reviews_dict = {}

    def general_reviews(self, name, phoneNumber, email, cleaninessGrade, serverGrade, treatmentGrade):
        """
        general_reviews -> Method checks if the required parameters are given and returns a message if they arent. It then
        checks the type of data given and if they are not the same as the expected datatypes it raises a type error. After
        that it check the values of the grades and phone number to see if they meet the requirement and if they do not it raises a
        value error. If all other conditions have been statisfied, it adds the customers info to the self.general_reviews_dict and
        appends it to the Reviews.general_reviews_list.
        """
        if name == None and phoneNumber == None and email == None:
            return "Invalid Review!/n Name and contact info must be written."
        if type(name) != str or type(phoneNumber) != str or type(email) != str or type(cleaninessGrade) != int or type(serverGrade) != int or type(treatmentGrade)!= int:
            raise TypeError
        if len(phoneNumber) != 10 or not(phoneNumber.isnumeric()):
            raise ValueError
        if (cleaninessGrade < 1 or cleaninessGrade > 5) or (serverGrade < 1 or serverGrade > 5) or (treatmentGrade < 1 or treatmentGrade > 5):
            raise ValueError
        else:
            self.general_reviews_dict = {"name": name, "number": phoneNumber, "email": email, "cleaniness grade": cleaninessGrade, "service grade": serverGrade, "treatment grade": treatmentGrade}
        Reviews.general_reviews_list.append(self.general_reviews_dict)

    def get_general_review(self, name):
        """
        get_general_review -> Method takes in a name parameter which it uses to check if the particular customer's review is in
        the Reviews.general_reviews_list. if the customer's review is in the list, you return the customer's review but if the
        review isnt, you return a message.
        """
        for reviews in Reviews.general_reviews_list:
            if reviews["name"] == name:
                return reviews
        return "Customer not found!"

    def items_review(self, name, phoneNumber , email, itemstasteGrade, serviceGrade, itemsSatisfactionGrade):
        """
        items_review -> Method checks if the required parameters are given and returns a message if they arent. It then
        checks the type of data given and if they are not the same as the expected datatypes it raises a type error. After
        that it check the values of the grades and phone number to see if they meet the requirement and if they do not it raises a
        value error. If all other conditions have been statisfied, it adds the customers info to the self.items_reviews_dict and
        appends it to the Reviews.items_reviews_list.
        """
        if name == None and phoneNumber == None and email == None:
            return "Invalid Review!/n Name and contact info must be written."
        if type(name) != str or type(phoneNumber) != str or type(email) != str or type(itemstasteGrade) != int or type(serviceGrade) != int or type(itemsSatisfactionGrade)!= int:
            raise TypeError
        if len(phoneNumber) != 10 or not(phoneNumber.isnumeric()):
            raise ValueError
        if (itemstasteGrade < 1 or itemstasteGrade > 5) or (serviceGrade < 1 or serviceGrade > 5) or (itemsSatisfactionGrade < 1 or itemsSatisfactionGrade > 5):
            raise ValueError
        else:
            self.items_reviews_dict  = {"name": name, "number": phoneNumber, "email": email, "cleaniness grade": itemstasteGrade, "service grade": serviceGrade, "treatment grade": itemsSatisfactionGrade}
        Reviews.items_reviews_list.append(self.items_reviews_dict )

    def get_items_review(self, name):
        """
        get_items_review -> Method takes in a name parameter which it uses to check if the particular customer's review is in
        the Reviews.items_reviews_list. if the customer's review is in the list, you return the customer's review but if the
        review isnt, you return a message.
        """
        for reviews in Reviews.items_reviews_list:
            if reviews["name"] == name:
                return reviews
        return "Customer not found!"