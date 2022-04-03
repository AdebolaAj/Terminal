class InventoryItem:

    def __init__(self, section, category, item, amount):

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

        if type(update_val) != int:
            raise TypeError("The update value should be an integer")
        if update_val <= 0:
            raise ValueError("The update value must be greater than 0")
        return self.amount >= update_val
            

    def RemoveAmount(self, update_val):

        if type(update_val) != int:
            raise TypeError("The update value should be an integer")
        if update_val <= 0:
            raise ValueError("The update value must be greater than 0")

        if self.CanRemoveAmount(update_val):
            self.amount -= update_val 

        else:
            raise ValueError(f"Unable to remove {update_val} since {self.section} -> {self.category} -> {self.item} only has {self.amount} in stock")


    def AddAmount(self, update_val):

        if type(update_val) != int:
            raise TypeError("The update value should be an integer")
        if update_val <= 0:
            raise ValueError("The update value must be greater than 0")

        self.amount += update_val

    def to_document(self):
        return {'section': self.section, 'category': self.category, 'item': self.item, 'amount': self.amount}

    @classmethod
    def from_document(cls, document):
        return InventoryItem(document['section'], document['category'], document['item'], document['amount'])