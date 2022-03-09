class Reviews:
  general_reviews_list = []
  items_reviews_list =[]
  def __init__(self):
    self.general_reviews_dict = {}
    self.items_reviews_dict = {}
    
  def general_reviews(self, name, number, email, cleaninessGrade, serverGrade, treatmentGrade):
    if name == None:
      return "Invalid Review!/n Name must be written."
    if number == None and email == None:
      answer = input("Are you sure you do not want to be contacted?/n Enter yes to continue or No to enter contact info: ")
      if answer.lower() == "yes":
        self.general_reviews_dict = {"name": name, "cleaniness grade": cleaninessGrade, "service grade": serverGrade, "treatment grade": treatmentGrade}
      else: 
        return "Invalid Review!/n No contact info."
    else:
      self.general_reviews_dict = {"name": name, "number": number, "email": email, "cleaniness grade": cleaninessGrade, "service grade": serverGrade, "treatment grade": treatmentGrade}
    Reviews.general_reviews_list.append(self.general_reviews_dict)

  def get_general_review(self, name):
    for reviews in Reviews.general_reviews_list:
      if reviews[name] == name:
        return reviews
    return "Customer not found!"
    
  def items_review(self, name, number, email, itemstasteGrade, serviceGrade, itemsSatisfactionGrade):
    if name == None:
      return "Invalid Review!/n Name must be written."
    if number == None and email == None:
      answer = input("Are you sure you do not want to be contacted?/n Enter yes to continue or No to enter contact info: ")
      if answer.lower() == "yes":
        self.items_reviews_dict  = {"name": name, "cleaniness grade": itemstasteGrade, "service grade": serviceGrade, "treatment grade": itemsSatisfactionGrade}
      else: 
        return "Invalid Review!/n No contact info."
    else:
      self.items_reviews_dict  = {"name": name, "number": number, "email": email, "cleaniness grade": itemstasteGrade, "service grade": serviceGrade, "treatment grade": itemsSatisfactionGrade}
    Reviews.items_reviews_list.append(self.items_reviews_dict )

  def get_items_review(self, name):
    for reviews in Reviews.items_reviews_list:
      if reviews[name] == name:
        return reviews
    return "Customer not found!"