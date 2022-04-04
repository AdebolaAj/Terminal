class ItemReview:
    """ItemReview is a class that represents an instance of an actual store item review.

    ItemReview objects can be generated, and each instance has six states;
    -The name
    -The phone number
    -The email
    -The item taste grade
    -The service grade
    -The item statisfaction grade

    Attributes:
        name: A string that represents the name of the person entering the review.
        phoneNumber: A string that represents the phone number of the person entering the review.
        email: A string that represents the email of the person entering the review.
        itemstasteGrade: A string that represents the items taste grade the person entering the review gives.
        serviceGrade: A string that represents the service grade the person entering the review gives.
        itemsSatisfactionGrade: A string that represents the items satisfaction grade the person entering the review gives.
    """
    def __init__(self, name, phoneNumber , email, itemstasteGrade, serviceGrade, itemsSatisfactionGrade):
        """
        ItemReview Constructor:
        self.name: The name asscociated with the GeneralReview object.
        self.phoneNumber: The phone number asscociated with the ItemReview object.
        self.email: The email asscociated with the ItemReview object.
        self.itemstasteGrade: The items taste grade asscociated with the ItemReview object.
        self.serviceGrade: The service grade asscociated with the ItemReview object.
        self.itemsSatisfactionGrade: The items satisfaction grade asscociated with the ItemReview object.
        """
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.itemstasteGrade = itemstasteGrade
        self.serviceGrade = serviceGrade
        self.itemsSatisfactionGrade = itemsSatisfactionGrade
    

    @classmethod
    def from_form(cls, form):
        """Creates a ItemReview object instance from values in a dictionary.

        Args:
            form (dict): The key-value pairs to be used to create the ItemReview object.

        Errors:
            Raises ValueError if document is None.
            Raises TypeError is name isnt all alphabetic
            Raises TypeError if the datatypes are not strings
            Raises ValueError if phone number is not within range
        Returns:
            ItemReview: A ItemReview object instance built with the values from document.
        """
        if form == None:
            raise ValueError("Form data must be provided")
        if not(all(letter.isalpha() or letter.isspace() for letter in form['name'])):
            raise TypeError("Name not the right format")
        elif int(form['phoneNumber']) > 10000000000 or int(form['phoneNumber']) <= 999999999:
            raise ValueError("Number not the right format")
        else:
            return cls(form['name'], form['phoneNumber'], form['email'], form['itemstasteGrade'], form['serviceGrade'], form['itemsSatisfactionGrade'])
    
    @classmethod
    def from_document(cls,document):
        """Creates a ItemReview object instance from values in a dictionary.

        Args:
            document (dict): The key-value pairs to be used to create the ItemReview object.
        Errors:
            Raises ValueError if document is None.
        Returns:
            or
            ItemReview: A GeneralReview object instance built with the values from document.
        """
        if document == None:
            raise ValueError("Document data must be provided")
        return cls(document['name'], document['phoneNumber'], document['email'], document['itemstasteGrade'], document['serviceGrade'], document['itemsSatisfactionGrade'])

    def to_document(self):
        """Converts a ItemReview object instance to a dictionary format.

        Returns:
            dict: A document representation of the ItemReview object instance.
        """
        return {'name':self.name, 'phoneNumber':self.phoneNumber, 'email':self.email, 'itemstasteGrade': self.itemstasteGrade, 'serviceGrade':self.serviceGrade, 'itemsSatisfactionGrade':self.itemsSatisfactionGrade}