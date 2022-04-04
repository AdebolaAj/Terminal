class InventoryItem:

    '''
    InventoryItem is a class that represents an instance of an item in an inventory. 

    InventoryItem objects can be generated, and each instance has 4 instances:
    - The section
    - The category
    - The item
    - The amount

    The attributes:
        section: a string that represents the specific section of an item in the inventory
        category: a string that represents the specific category of an item in the inventory
        item: a string that represents the actual name of an item in the inventory 
        amount: an integer that represents the amount of an item left in the inventory
    '''    

    def __init__(self, section, category, item, amount):

        '''Constructor for the InventoryItem object with a section string, category string, item string, and an amount integer.

        Args:
            section(string): the section of an item in the inventory (the first layer)
            category(string): the category of an item in the inventory  (the second layer)
            item(string): the actual name of an item (the third layer)
            amount(integer): the count of an item in the inventory

        Returns:
            no return(void)
        '''

        if type(section) != str:
            raise TypeError("The section must be a string")
        if type(category) != str:
            raise TypeError("The category must be a string")
        if type(item) != str:
            raise TypeError("The item must be a string")
        if type(amount) != int:
            raise TypeError("The amount must be an integer")
        if amount < 0:
            raise ValueError("The amount cannot be less than zero")


        self.section = section
        self.category = category
        self.item = item
        self.amount = amount 

    def CanRemoveAmount(self, update_val):

        '''Checks to see if a specified amount of an item can be removed from the inventory

        Args:
            update_val(int): the amount of an item that has to be removed

        Returns:
            boolean: True if the number can be removed, False if it cannot be removed.
        '''

        if type(update_val) != int:
            raise TypeError("The update value should be an integer")
        if update_val <= 0:
            raise ValueError("The update value must be greater than 0")
        return self.amount >= update_val
            

    def RemoveAmount(self, update_val):

        '''Removes a specific amount of an item from the inventory.

        Args:
            update_val(int): the amount to be removed from an item's amount in the inventory.

        Returns:
            no return (void)
        '''

        if type(update_val) != int:
            raise TypeError("The update value should be an integer")
        if update_val <= 0:
            raise ValueError("The update value must be greater than 0")

        if self.CanRemoveAmount(update_val):
            self.amount -= update_val 

        else:
            raise ValueError(f"Unable to remove {update_val} since {self.section} -> {self.category} -> {self.item} only has {self.amount} in stock")


    def AddAmount(self, update_val):

        '''Adds a specified amount to the amount of an item in the inventory

        Args:
            update_val(int): the amount to be added to the item's amount in inventory

        Returns:
            No return (void)
        '''

        if type(update_val) != int:
            raise TypeError("The update value should be an integer")
        if update_val <= 0:
            raise ValueError("The update value must be greater than 0")

        self.amount += update_val

    def to_document(self):

        '''Converts an InventoryItem object instance to a dictionary format.

        Returns:
            dict: A document representation of the InventoryItem object instance.
        '''

        return {'section': self.section, 'category': self.category, 'item': self.item, 'amount': self.amount}

    @classmethod
    def from_document(cls, document):

        '''Creates a InventoryItem object instance from values in a dictionary.

        Args:
            document (dict): The key-value pairs to be used to create the InventoryItem object.
        Returns:
            InventoryItem: An InventoryItem object instance built with the values from document.
        '''

        if type(document) != dict:
            raise TypeError("The document must be a dictionary")
        
        keys = []
        for key in document.keys():
            if type(key) == str and key.isalpha():
                keys.append(key.lower())
            else:
                keys.append(key)

        if 'section' not in keys:
            raise KeyError("The key 'section' does not exist in the document")
        if 'category' not in keys:
            raise KeyError("The key 'category' does not exist in the document")
        if 'item' not in keys:
            raise KeyError("The key 'item' does not exist in the document")
        if 'amount' not in keys:
            raise KeyError("The key 'amount' does not exist in the document")

        return InventoryItem(document['section'], document['category'], document['item'], document['amount'])