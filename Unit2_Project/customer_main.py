from giftcards import *

customers_attempted = set() #set of phone numbers of customers who have attempted the trivia for the day, return to empty set once employee changes answer for the day
running = True

while running:
    print("Would you like to leave a review(1), redeem a giftcard(2), or try out for a giftcard (3)? Enter 'logout' to logout") #customer accessible operations
    user_input = input("> ")

    if user_input == "1":
        pass
    elif user_input == "2":
        user_code = input("Enter the giftcard code: ")
        redeem_code = Giftcard().redeem(user_code)
        print(redeem_code)
    elif user_input == "3":
        user_phone_number = input("Enter your phone number: ")
        if user_phone_number.isdigit():
            if user_phone_number in customers_attempted:
                print("You can only attempt to win a giftcard once a day")
            else:
                customers_attempted.add(user_phone_number)
                user_guess = input("Enter your answer to today's trivia question\nThe question can be found in store: ")
                if user_guess.lower() == Giftcard.trivia_solution.lower():
                    card_n = Giftcard()
                    print(f'Congrats! You got the answer right. Your giftcard code is {card_n.gift_code}')
                else:
                    print("Sorry, your response was incorrect. Try again tomorrow")
        else:
            print("Your phone number is invalid, please ensure you only type in numbers and no (+) sign")
    elif user_input.lower() == "logout":
        running = False
    else:
        print("Invalid input")
