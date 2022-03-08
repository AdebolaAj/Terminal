from giftcards import *

running = True

while running:
    print("Would you like to set today's trivia answer(1)? Enter 'logout' to logout") #admin accessible operations
    user_input = input("> ")

    if user_input == "1": 
        new_trivia_answer = input("What is the answer for today's trivia question? ")
        Giftcard.set_trivia_solution(new_trivia_answer)
    elif user_input.lower() == "logout":
        running = False
    else:
        print("Invalid input")
