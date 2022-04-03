class GeneralReview:
    """
    Reviews class Attributes:
    general_reviews_list -> a list which stores all the general reviews left by customers which the employees use to access
    a particluar customers review.
    items_reviews_list -> a list which stores all the item reviews left by customers which the employees use to access
    what customers think of our products.
    """
    def __init__(self, name, phoneNumber, email, cleaninessGrade, serverGrade, treatmentGrade):
        """
        Reviews Constructor:
        self.general_reviews_dict: A dictionary which stores each customer's general review.
        self.items_reviews_dict: A dictionary which stores each customer's items review.
        """
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.cleaninessGrade = cleaninessGrade
        self.serverGrade = serverGrade
        self.treatmentGrade = treatmentGrade
    
    @classmethod
    def from_form(cls, form):
        if form['name'].isalpha():
            raise TypeError("Name not the right format")
        elif form['phoneNumber'] < 0:
            raise ValueError("Number not the right format")
        else:
            return cls(form['name'], form['phoneNumber'], form['email'], form['cleaninessGrade'], form['serverGrade'], form['treatmentGrade'])
    
    @classmethod
    def from_document(cls,document):
        return cls(document['name'], document['phoneNumber'], document['email'], document['cleaninessGrade'], document['serverGrade'], document['treatmentGrade'])

    def to_document(self):
        return {'name':self.name, 'phoneNumber':self.phoneNumber, 'email':self.email, 'cleaninessGrade': self.cleaninessGrade, 'serverGrade':self.serverGrade, 'treatmentGrade':self.treatmentGrade}


    