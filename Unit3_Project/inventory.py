class Inventory:

    def __init__(self, section, category, item, amount):

        self.section = section
        self.category = category
        self.item = item
        self.amount = amount 

    def CanRemoveAmount(self, updt_val):
        
        return self.amount >= updt_val

    def RemoveAmount(self, updt_val):

        if self.CanRemoveAmount(updt_val):
            self.amount -= updt_val            

    def AddAmount(self, updt_val):

        self.amount += updt_val

    # def FilterValue(self):
    #     return {'section': self.section, 'category': self.category, 'item': self.item, 'amount': self.amount}

    @staticmethod
    def from_document(document):
        return Inventory(document['section'], document['category'], document['item'], document['amount'])