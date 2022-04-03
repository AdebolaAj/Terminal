import random
import re


class Giftcard:
    """
    Giftcard is a class that represents an instance of an actual store giftcard.

    Giftcard objects can be generated, and each instance has three states;
    -The giftcode
    -The gift value
    -The redeem state

    Attributes:
        gift_code: A string that represents the actual giftcard code that can be redeemed for a value.
        gift_value: A string that represents the value attached to a particular giftcard code.
        redeem_state: A boolean indicating whether a giftcard has been used or not.
    """
    giftcard_values = ["20% off any total order", "1 free beverage and sweet item", "1 free Thursday lunch combo", "Free Sunday brunch combo for 2", "10% off a savory item", "2 items for the price of 1"]

    def __init__(self, gift_code, gift_value, redeem_state=False):
        """
        Constructor for Giftcard object with a gift_code string, a gift_value string, and an optional redeem_state boolean.

        Args:
            self: Object instance.
            gift_code (str): The giftcode associated with a Giftcard object.
            gift_value (str): The value associated with a Giftcard object.
            redeem_state (bool): Indicates whether card has been used or not. Default value False
        """
        if type(gift_code) != str or type(gift_value) != str:
            raise TypeError('Both giftcode and gift_value have to be strings.')
        if type(redeem_state) != bool:
            raise TypeError('redeem_state should be a boolean.')
        self.gift_code = gift_code
        self.gift_value = gift_value
        self.redeem_state = redeem_state 
    
    @staticmethod
    def generate_code() -> str:
        """
        Creates a random giftcard code to be associated with a giftcard object.

        Args:
            None
        Returns:
            code (str): The generated giftcode to be associated with a giftcard object instance.
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
        Determines valadity of a giftcard code by checking if it matches a pre-determined pattern.

        Args:
            code_to_verify (str): The giftcard code to be authenticated.
        Returns:
            bool: The validity of the giftcode.
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
        Sets the redeem_state of a Giftcard object instace to indicate it has been used.

        Args:
            self: Object instance.
        Returns:
            gift_value (str): The value of a Giftcard object, if it has not been previously used.
            None: No value becuase the giftcard has been previously redeemed.
        """
        if not self.redeem_state:        
            self.redeem_state = True
            return self.gift_value
        else:
            return None

    def __str__(self):
        """
        Represents a Giftcard object instance as a string.

        Args:
            self: Object instance.
        Returns:
            str: Contains details about a Giftcard object's code, value and redeem state.
        """
        return f'{self.gift_code}, {self.gift_value}, {"Redeemed" if self.redeem_state else "Not redeemed"}'
    
    def to_document(self):
        """
        Converts a Giftcard object instance to a dictionary format.

        Args:
            self: Object instance.
        Returns:
            dict: A dictionary representation of the Giftcard object instance.
        """
        return {"giftcode": self.gift_code, "gift_value": self.gift_value, "redeem_state": self.redeem_state}

    @staticmethod
    def from_document(document):
        """
        Creates a Giftcard object instance from values in a dictionary.

        Args:
            document (dict): The key-value pairs to be used to create the Giftcard object.
        Returns:
            Giftcard: A Giftcard object instance built with the values from document.
        """
        if type(document) != dict:
            raise TypeError('Document should be a dictionary.')

        return Giftcard(document["giftcode"], document["gift_value"], document["redeem_state"])

    @classmethod
    def create_new(cls):
        """
        Creates a new Giftcard object instance with the class method and class attribute.

        Args:
            cls: Object class.
        Returns:
            Giftcard: A Giftcard object instance built with the class method and attribute.
        """
        return cls(cls.generate_code(), random.choice(cls.giftcard_values))

