from giftcards import *
from inventory import *

running = True
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

employee = Inventory(first_name, last_name)

def verify_item(obj):

    while True:

        print("Enter a section: ")
        obj.get_section()
        section = input()

        if obj.section_valid(section):
            break

        else:
            print("That is not a valid section, enter 1 to exit")
            exit = input()
            if exit == '1':
                return None

    while True:

        print("Enter a category: ")
        obj.get_category(section)
        category = input()

        if obj.category_valid(section, category):
            break

        else:
            print("That is not a valid category, enter 1 to exit")
            exit = input()
            if exit == '1':
                return None

    while True:

        print("Enter an item: ")
        obj.get_items(section, category)
        item = input()

        if obj.item_valid(section, category, item):
            break

        else:
            print("That is not a valid item, enter 1 to exit")
            exit = input()
            if exit == '1':
                return None

    return [section, category, item]


while running:

    action = input("What would you like to do?\nEnter 1 to set today's trivia answer.\nEnter 2 to update the inventory\nEnter 3 to inquire about an item's stock in the inventory\nEnter 'logout' to logout\n")

    if action == "1":
        new_trivia_answer = input("What is the answer for today's trivia question? ")
        Giftcard.set_trivia_solution(new_trivia_answer)

    elif action == "2":
        
        update_action = input("Enter 1 to add existing item stocks to the inventory\nEnter 2 to remove existing item stocks from the inventory\n")

        if update_action == '1':

            while True:
            
                updt_itm = verify_item(employee)

                if updt_itm == None:
                    break

                else:
                    
                    amount = input("How many of this item are you adding?")
                    print(employee.add_stock(updt_itm[0], updt_itm[1], updt_itm[2], int(amount)))

                finished = input("Enter 1 to add to another item's inventory or 0 to stop\n")

                if finished == '0':
                    break

        elif update_action == '2':
            
            while True:
            
                updt_itm = verify_item(employee)

                if updt_itm == None:
                    break

                else:
                    
                    amount = input("How many of this item are you removing?")
                    print(employee.remove_stock(updt_itm[0], updt_itm[1], updt_itm[2], int(amount)))

                finished = input("Enter 1 to remove from another item's inventory or 0 to stop\n")

                if finished == '0':
                    break

        else:
            print("That is not a valid input")

    elif action =="3":

        while True:
            
                updt_itm = verify_item(employee)

                if updt_itm == None:
                    break

                else:
                    
                    amount = employee.get_item_count(updt_itm[0], updt_itm[1], updt_itm[2])
                    print(updt_itm[2] + ": " + str(amount))

                finished = input("Enter 1 to inquire about another item's inventory or 0 to stop\n")

                if finished == '0':
                    break

    elif action == "logout":
        running = False
    
    else:
        print("That is not a valid input")
        