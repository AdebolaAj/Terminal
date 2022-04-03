from customer_reviews import * 


customer1 = Reviews()
customer2 = Reviews()
customer3 = Reviews()
customer4 = Reviews()
customer5= Reviews()

customer1.general_reviews("Patrick", "8192104615", "patrick@gmail.com", 5, 4, 5)
customer2.general_reviews("Alyssa", "7102487366", "alyssa@gmail.com", 4, 5, 3)
customer3.general_reviews("Jose", "7328449299", "jose@gmail.com", 4, 4, 4)
customer4.general_reviews("Karen", "8773934443", "karen@gmail.com", 1, 1, 1)

print(customer2.get_general_review("Alyssa"))