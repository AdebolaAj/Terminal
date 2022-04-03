class ItemReview:
    """
    Reviews class Attributes:
    general_reviews_list -> a list which stores all the general reviews left by customers which the employees use to access
    a particluar customers review.
    items_reviews_list -> a list which stores all the item reviews left by customers which the employees use to access
    what customers think of our products.
    """
    def __init__(self, name, phoneNumber , email, itemstasteGrade, serviceGrade, itemsSatisfactionGrade):
        """
        Reviews Constructor:
        self.general_reviews_dict: A dictionary which stores each customer's general review.
        self.items_reviews_dict: A dictionary which stores each customer's items review.
        """
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.itemstasteGrade = itemstasteGrade
        self.serviceGrade = serviceGrade
        self.itemsSatisfactionGrade = itemsSatisfactionGrade
    

    @classmethod
    def from_form(cls, form):
        if form == None:
            raise ValueError("Form data must be provided")
        if not (form['name'].isalpha()):
            raise TypeError("Name not the right format")
        elif form['phoneNumber'] < 0:
            raise ValueError("Number not the right format")
        else:
            return cls(form['name'], form['phoneNumber'], form['email'], form['itemstasteGrade'], form['serviceGrade'], form['itemsSatisfactionGrade'])
    
    @classmethod
    def from_document(cls,document):
        if document == None:
            raise ValueError("Document data must be provided")
        return cls(document['name'], document['phoneNumber'], document['email'], document['itemstasteGrade'], document['serviceGrade'], document['itemsSatisfactionGrade'])

    def to_document(self):
        return {'name':self.name, 'phoneNumber':self.phoneNumber, 'email':self.email, 'itemstasteGrade': self.itemstasteGrade, 'serviceGrade':self.serviceGrade, 'itemsSatisfactionGrade':self.itemsSatisfactionGrade}