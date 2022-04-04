class GeneralReview:
    """GeneralReview is a class that represents an instance of an actual store general review.

    GeneralReview objects can be generated, and each instance has six states;
    -The name
    -The phone number
    -The email
    -The cleaniness grade
    -The server grade
    -The treatment grade

    Attributes:
        name: A string that represents the name of the person entering the review.
        phoneNumber: A string that represents the phone number of the person entering the review.
        email: A string that represents the email of the person entering the review.
        cleaninessGrade: A string that represents the cleaniness grade the person entering the review gives.
        serverGrade: A string that represents the server grade the person entering the review gives.
        treatmentGrade: A string that represents the treatment grade the person entering the review gives.
    """

    def __init__(self, name, phoneNumber, email, cleaninessGrade, serverGrade, treatmentGrade):
        """
        Constructor for GeneralReview object with a name, phoneNumber, email, cleaninessGrade, serverGrade and treatmentGrade.

        Args:
            self.name (str): The name asscociated with the GeneralReview object.
            self.phoneNumber (str): The phone number asscociated with the GeneralReview object.
            self.email (str): The email asscociated with the GeneralReview object.
            self.cleaninessGrade (str): The cleaniness Grade asscociated with the GeneralReview object.
            self.serverGrade (str): The server Grade asscociated with the GeneralReview object.
            self.treatmentGrade (str): The treatment Grade asscociated with the GeneralReview object.
        """
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.cleaninessGrade = cleaninessGrade
        self.serverGrade = serverGrade
        self.treatmentGrade = treatmentGrade
    
    @classmethod
    def from_form(cls, form):
        """Creates a GeneralReview object instance from values in a dictionary.

        Args:
            form (dict): The key-value pairs to be used to create the GeneralReview object.

        Errors:
            Raises ValueError if document is None.
            Raises TypeError is name isnt all alphabetic
            Raises TypeError if the datatypes are not strings
            Raises ValueError if phone number is not within range
        Returns:
            GeneralReview: A ItemReview object instance built with the values from document.
        """
        if form == None:
            raise ValueError("Form data must be provided")
        if not(all(letter.isalpha() or letter.isspace() for letter in form['name'])):
            raise TypeError("Name not the right format")
        if type(form['phoneNumber']) != str or type(form['email']) != str or type(form['cleaninessGrade']) != str or type(form['serverGrade']) != str or type(form['treatmentGrade']) != str: 
            raise TypeError("Invalid format")
        elif int(form['phoneNumber']) > 10000000000 or int(form['phoneNumber']) <= 999999999:
            raise ValueError("Number not the right format")
        else:
            return cls(form['name'], form['phoneNumber'], form['email'], form['cleaninessGrade'], form['serverGrade'], form['treatmentGrade'])
    
    @classmethod
    def from_document(cls,document):
        """Creates a GeneralReview object instance from values in a dictionary.

        Args:
            document (dict): The key-value pairs to be used to create the GeneralReview object.
        Errors:
            Raises ValueError if document is None.
        Returns:
            or
            GeneralReview: A GeneralReview object instance built with the values from document.
        """
        if document == None:
            raise ValueError("Form data must be provided")
        return cls(document['name'], document['phoneNumber'], document['email'], document['cleaninessGrade'], document['serverGrade'], document['treatmentGrade'])

    def to_document(self):
        """Converts a GeneralReview object instance to a dictionary format.

        Returns:
            dict: A document representation of the GeneralReview object instance.
        """
        return {'name':self.name, 'phoneNumber':self.phoneNumber, 'email':self.email, 'cleaninessGrade': self.cleaninessGrade, 'serverGrade':self.serverGrade, 'treatmentGrade':self.treatmentGrade}


    