import random
import re
import pymongo
import os


class Giftcard:
    """
    Giftcard class Attributes
    trivia_solution: A string that is the answer to the trivia of the day for a chance to win a free giftcard code.
    generated_giftcards: A dictionary with created giftcard_code -> giftcard_object key -> value pairs.
    giftcard_values: A list of strings that are the possible rewards for a giftcard code.
    """
    giftcard_values = ["20% off any total order", "1 free beverage and sweet item", "1 free Thursday lunch combo", "Free Sunday brunch combo for 2", "10% off a savory item", "2 items for the price of 1"]

    def __init__(self, gift_code, gift_value, redeem_state=False):
        """
        Giftcard Constructor
        self.gift_code: A string that is the giftcard code that is generated when the Giftcard object is created.
        self.gift_value: A string that is the value to be received after redeeming a giftcard code.
        self.redeem_state: A boolean that represents whether a giftcard code has been redeemed or not. True for "redeemed", False for "not redeemed"
        """
        self.gift_code = gift_code
        self.gift_value = gift_value
        self.redeem_state = redeem_state 
    
    @staticmethod
    def generate_code() -> str:
        """
        generate_code: Method that returns a valid giftcard code as a string that would be assigned to a Giftcard object upon creation.
        first: A string that is the first of three parts of a valid giftcard code. Composed of alphanumeric characters.
        second: A string that is the second of three parts of a valid giftcard code. Composed of alphanumeric characters.
        third: A string that is the third of three parts of a valid giftcard code. Composed of alphanumeric characters.
        code: A string that is the giftcard card code assigned to a Giftcard object upon creation.
        """
        uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowers = "abcdefghijklmnopqrstuvwxyz"
        digits = "0123456789"

        first = random.choice(uppers) + random.choice(digits) + random.choice(lowers) + random.choice(digits)
        second = random.choice(lowers) + random.choice(digits) + random.choice(lowers) + random.choice(uppers)
        third = random.choice(digits) + random.choice(uppers) + random.choice(lowers) + random.choice(uppers)
        
        code = f'{first}-{second}-{third}'
        return code

    @staticmethod  
    def authenticate(code_to_verify): 
        """
        authenticate: Method that takes in a giftcard code as a string, and returns a boolean, True if the code is valid, and False if the code is invalid.
        code_to_verify: A string that is the giftcard code to be verified for authenticity.
        code_matches_pattern: A boolean that represents the validity of a giftcard code. True if the code is valid, and False if the code is invalid.
        """
        if type(code_to_verify) != str:
            raise TypeError("The giftcard code should be a string")

        code_matches_pattern = bool(re.match("[A-Z][0-9][a-z][0-9]-[a-z][0-9][a-z][A-Z]-[0-9][A-Z][a-z][A-Z]", code_to_verify))
        if not code_matches_pattern:
            return False
        else:
            return True
    
    def redeem(self):
        """
        redeem: Method that takes in a giftcard code as a string, and returns the value of the giftcard if the code is valid, or a error message if otherwise.
        code_to_redeem: A string that is the giftcard code to be redeemed for a value.
        """
        if not self.redeem_state:        
            self.redeem_state = True
            return self.gift_value
        else:
            return None

    def __str__(self):
        """
        String representation method: Returns a string that gives information about the giftcard code, gift value and redeem state of a Giftcard object. For debugging
        """
        return f'{self.gift_code}, {self.gift_value}, {"Redeemed" if self.redeem_state else "Not redeemed"}'
    
    def to_document(self):
        return {"giftcode": self.gift_code, "gift_value": self.gift_value, "redeem_state": self.redeem_state}

    @staticmethod
    def from_document(document):
        return Giftcard(document["giftcode"], document["gift_value"], document["redeem_state"])

    @classmethod
    def create_new(cls):
        return cls(cls.generate_code(), random.choice(cls.giftcard_values))

