from datetime import datetime
import pymongo 
class Inventory:
    '''
    This class allows employees to manage the inventory of Terminally Latte. The employees can update the inventory by adding or removing stock from the menu list and can also check to see if an order can be fulfilled based on the current inventory. The employees are required to enter their first and last name when accessing the inventory. Every addition and removal of stock in the inventory will be recorded by using the person responsible for the altering of the inventory and the date and time this alteration was made.
    '''
    # class Update:
    #     def __init__(self, name, additions, removals):

    #         self.name = name
    #         self.additions = additions
    #         self.removals = removals 

            
    update_track = {}  #dictionary to keep track of which employee updated the inventory and how they updated the inventory
    menu_count = { #dictionary that keeps track of the menu items and their stock count * all lowercase
    "beverages": {
        
        "black coffee":{"hot": 0, "with ice": 0},
        "hot chocolate": {"with milk": 0, "without milk": 0},
        "milkshakes": {"vanilla": 0, "chocolate": 0, "strawberry": 0},
        "smoothies": {"strawberry-banana": 0, "mango-pineapple": 0},
        "fruit juice": {"orange": 0, "apple": 0, "mango": 0}
    },

    "sweet foods": {
        
        "muffins": {"chocolate milk": 0, "blueberry": 0},
        "pies": {"apple pie": 0, "cranberry pie": 0},
        "cheesecakes": {"strawberry": 0, "chocolate": 0, "key-lime": 0},
        "cookies": {"chocolate chip": 0, "double chocolate chip": 0, "oatmeal raisin": 0},
        "donuts": {"glazed": 0, "sprinkled": 0, "sugar": 0, "powdered": 0, "jelly filled": 0}
    },

    "savory foods": {
        
        "handmade wraps": {"veggie": 0, "chicken": 0, "turkey": 0},
        "homemade sandwiches": {"chicken": 0, "blt": 0, "bacon egg and cheese": 0},
        "fresh bagels": {"plain": 0, "poppyseed": 0, "garlic": 0, "creamcheese": 0},
        "crepes": {"egg ham and cheese": 0, "spinach artichoke": 0, "spinach bacon": 0, "vegan chickpea": 0},
        "omlettes": {"plain": 0, "shredded cheese": 0, "diced onions": 0, "diced tomatoes": 0, "chopped spinach": 0, "chopped red and green peppers": 0, "fresh lettuce": 0, "crispy bacon": 0, "glazed ham": 0}
    }
    }
  

    def __init__(self, f_name, l_name):

        '''
        initializer that takes in two strings. The first string in the parameter list represents the employee's first name and the second string in the parameter list represents the employee's last name. If either of these paramters are not of type string, a type error should be raised. The first name and last name strings are used to concatenate the employee's full name. Once the employee's full name is concatenated, the employee's full name is used to create a key in the class variable "update_track" - using this syntax {"full employee name": {"add": [], "remove": []}} - in order for every update the employee makes to be recorded accurately. 
        '''

        if type(f_name) != str:
            raise TypeError("first name should be of type string")

        if type(l_name) != str:
            raise TypeError("last name should be of type string")
            #57 ->  "57"

        self.f_name = f_name.lower()
        self.l_name = l_name.lower()
        self.full_name = f_name + " " + l_name
        Inventory.update_track[self.full_name] = {"add": [], "remove": []}

    @staticmethod
    def get_section():
        '''
        This method takes in no parameters. The method prints all of the sections present in the inventory.
        '''
        count = 1
        for i in Inventory.menu_count.keys():
            print(str(count) + ". " + i)
            count += 1

    @staticmethod
    def section_valid(section):

        '''
        This method verifies that the section the employee wishes to alter the stocks of is actually present in the inventory. It takes in the name of the section desired by the employee as a parameter (a string) and returns a boolean value that represents whether or not the section is actually present. Returns True if the section is valid and False if the section is invalid. If the section is not of type string, a type error should be raised. However, if a string is passed into the method the string is converted to lowercase to maintain consistencies with how the menu is stored. 
        '''

        if type(section) != str:
            raise TypeError("section has to be of type string")

        section = section.lower()

        if section in Inventory.menu_count:
            return True

        else:
            return False

    @staticmethod
    def category_valid(section, category):

        '''
        This method verifies that the category the employee wishes to alter the stocks of is actually present in the inventory. It takes in the name of the section (a string) and the name of the category (a string) desired by the employee as parameters, and returns a boolean value that represents whether or not the category is actually present in the specific section. Returns True if the category is valid in the specific section and False if the category is invalid in the specific section. If the section or category is not of type string, a type error should be raised. However, if two strings are passed into the method the strings are converted to lowercase to maintain consistencies with how the menu is stored. 
        '''

        if type(section) != str:
            raise TypeError("section should be a string")

        if type(category) != str:
            raise TypeError("category should be a string")

        section = section.lower()
        category = category.lower()

        if Inventory.section_valid(section) and category in Inventory.menu_count[section]:
            return True

        else:
            return False

    @staticmethod
    def get_category(section):

        '''
        This method takes in one parameter which represents a section in the inventory and prints all the categories present in the section. 
        This method utilizes the secton_valid method to ensure that the parameter is a valid section in the inventory. 
        If the section parameter is invalid, a value error is raised.
        '''

        if Inventory.section_valid(section):
            count = 1
            section = section.lower()
            for i in Inventory.menu_count[section].keys():
                print(str(count) + ". " + i)
                count += 1

        else:
            raise ValueError("Section is not a valid section")

    @staticmethod
    def item_valid(section, category, item):

        '''
        This method verifies that the item the employee wishes to alter the stocks of is actually present in the inventory. It takes in the name of the section (a string), the name of the category (a string), the actual item (a string) desired by the employee as parameters, and returns a boolean value that represents whether or not the item is actually present in the specific section and category. Returns True if the item is valid in the specified section and category but False if the item is invalid in the specific section and category. If the item, section, or category is not of type string, a type error should be raised. However, if three strings are passed into the method the strings are converted to lowercase to maintain consistencies with how the menu is stored. 
        '''

        if type(section) != str:
            raise TypeError("section should be a string")

        if type(category) != str:
            raise TypeError("category should be a string")

        if type(item) != str:
            raise TypeError("item should be a string")

        section = section.lower()
        category = category.lower()
        item = item.lower()

        if item in Inventory.menu_count[section][category]:
            return True

        else:
            return False

    @staticmethod
    def get_items(section, category):

        '''
        This method takes two parameters the first to represent a section in the inventory and the second to represent a category in the inventory
        Then the items present in the category in the inventory are printed. If the category is invalid a value error is raised.
        '''

        if Inventory.category_valid(section, category):
            count = 1
            section = section.lower()
            category = category.lower()            

            for i in Inventory.menu_count[section][category].keys():
                print(str(count) + ". " + i)
                count += 1

        else:
            raise ValueError("Category is not a valid category")

    @staticmethod
    def overall_item_exists(section, category, item):

        '''
        This method utilizes the previous methods to verify sections, categories, and items in the inventory. This function calls on each method, section_valid first, category_valid second, and item_valid third in order to have an overall check with one function. A boolean value is returned that represents whether or not the item is present in the inventory as it relates to the specified category and section. The method requires three strings to be entered, first representing section (string), second representing category(string), and third representing the item(string). If any of these values passed in are not a string a type error should be raised. 
        '''

        if type(section) != str:
            raise TypeError("section should be a string")

        if type(category) != str:
            raise TypeError("category should be a string")

        if type(item) != str:
            raise TypeError("item should be a string")

        section = section.lower()
        category = category.lower()
        item = item.lower()

        if Inventory.section_valid(section):

            if Inventory.category_valid(section, category):

                if Inventory.item_valid(section, category, item):
                    return True

                else:
                    return False       

            else:
                return False

        else:
            return False
      

    @staticmethod
    def get_item_count(section, category, item):

        '''
        This method allows the user to get the current inventory value(integer) for a specific item. It uses the previous functions to verify that the employee is actually inquiring about a valid menu item. If the employee is not inquiring about a valid menu item a string should be returned informing the employee that the specified menu item does not exist. However, if the menu item is valid, an integer representing the specified menu item's count in the inventory is returned. Because the previous methods are being used, if any of the parameters are not strings, a type error is raised. *All parameters must be converted to lowercase to avoid errors once they are verified to be strings*
        '''

        if Inventory.overall_item_exists(section, category, item):
            section = section.lower()
            category = category.lower()
            item = item.lower()

            return Inventory.menu_count[section][category][item]

        else:
            return "Item does not exist"
      

    def __update_tracker(self, section, category, item, value, action):

        '''
        This method takes in 5 parameters and does not return any value. This method serves to update the inventory based on the employee's preferences. The parameters section, category, and item variable are used to access the specific inventory value the employee would like to update. The value parameter represents the number the employee would like to alter the current inventory of the specified item by. The action parameter is a string that represents whether or not the employee would like to increment ("add") or decrement ("remove") the specified item in the inventory by. Type errors are raised if either the section, category, item, or action paramters are not of type strings or the value parameter is not of type integer. Also, if the value parameter is less than 1 a value error is raised. 

        Once the inventory is updated, the time and action of the user is recorded in the update_track class variable.
        '''

        if type(section) != str:
            raise TypeError("section must be a string")

        if type(category) != str:
            raise TypeError("category must be a string")

        if type(item) != str:
            raise TypeError("item must be a string")

        if type(value) != int:
            raise TypeError("value must be an integer")

        if value < 1:
            raise ValueError("The value must be greater than 0")

        if type(action) != str:
            raise TypeError("action must be a string")

        section = section.lower()
        category = category.lower()
        item = item.lower()

        if action == "add":

            if self.full_name in Inventory.update_track:

                current_time = datetime.now().strftime("%x") + " at " + datetime.now().strftime("%X")
                current_entry = {current_time: (section + " -> " + category + " -> " + item, value)}

                Inventory.update_track[self.full_name]["add"].append(current_entry)
            

        else:
            current_time = datetime.now().strftime("%x") + " at " + datetime.now().strftime("%X")
            current_entry = {current_time: (section + " -> " + category + " -> " + item, value)}

            Inventory.update_track[self.full_name]["remove"].append(current_entry)


    def add_stock(self, section, category, item, value):    

        '''
        This method is used to add to the current stock in the inventory of a specific menu item. The method has 4 parameters. The first three parameters represent the section(string), category(string), and item(string) respectively of the item's inventory to be added to. The fourth parameter represents the value that the item's stock is meant to be incremented by. Type errors are raised if either the section, catgory, or item parameters are not of type string. A value error is raised if the value parameter is less than 1. The update_tracker method is called using the same parameters of this method with the addition of the string "add" in order to increment the desired item's inventory value. Once the stock number of the item has been incremented in the inventory, a string is returned informing the employee that the item has been incremented by the specified number. 
        '''

        if type(section) != str:
            raise TypeError("section must be a string")

        if type(category) != str:
            raise TypeError("category must be a string")

        if type(item) != str:
            raise TypeError("item must be a string")

        if type(value) != int:
            raise TypeError("value must be an integer")

        section = section.lower()
        category = category.lower()
        item = item.lower()

        if value > 0:
            Inventory.menu_count[section][category][item] += value
            self.__update_tracker(section, category, item, value, "add")
            return item + " has been incremented by " + str(value)
            

        else:
            raise ValueError("The value must be greater than 0")


    
    @staticmethod
    def order_fulfilled(section, category, item, value):

        '''
        This method allows the employee to check whether or not an order can be fulfilled. This method returns a boolean value - True if the order can be fulfilled and false if the order can't be fulfilled. The first three paramters represent the section(string), category(string), and item(string) respectively to be checked. The value parameter (integer) represents the value of the specific item that is being checked. If the value parameter is less than or equal to the number of stock present for the specified item in the inventory True is returned, otherwise False is returned. A value error is raised if the value parameter is less than 1. Type errors are raised if the section, category, or item parameters are not of type string or if the value parameter is not of type integer. 
        '''

        if type(section) != str:
            raise TypeError("section must be a string")

        if type(category) != str:
            raise TypeError("category must be a string")

        if type(item) != str:
            raise TypeError("item must be a string")

        if type(value) != int:
            raise TypeError("value must be an integer")

        if value < 1:
            raise ValueError("value must be greater than 0")

        section = section.lower()
        category = category.lower()
        item = item.lower()

        if Inventory.menu_count[section][category][item] >= value:
            return True

        else:
            return False


    def remove_stock(self, section, category, item, value):

        '''
        This method is used to remove from the current stock in the inventory of a specific menu item. The method has 4 parameters. The first three parameters represent the section(string), category(string), and item(string) respectively of the item's inventory to be removed from. The fourth parameter represents the value that the item's stock is meant to be decremented by. Type errors are raised if either the section, catgory, or item parameters are not of type string. A value error is raised if the value parameter is less than 1. The update_tracker method is called using the same parameters of this method with the addition of the string "remove" in order to decrement the desired item's inventory value. 

        The order fulfilled method is called to verify that the value to be decremented by is possible. If the value to be decremented by is not possible, a string is returned informing that it is not possible to decrement that item by the specified value. If it is possible, a string is returned informing the employee that the item's stock number has been decremented by the specified amount.
        '''

        if type(section) != str:
            raise TypeError("section must be a string")

        if type(category) != str:
            raise TypeError("category must be a string")

        if type(item) != str:
            raise TypeError("item must be a string")

        if type(value) != int:
            raise TypeError("value must be an integer")

        section = section.lower()
        category = category.lower()
        item = item.lower()

        if value > 0:
            
            if Inventory.order_fulfilled(section, category, item, value):
                Inventory.menu_count[section][category][item] -= value
                self.__update_tracker(section, category, item, value, "remove")
                return item + " has been decremented by " + str(value)
            

            else:
                return "There is not enough " + item + " to decrement"

        else:
            raise ValueError("The value must be greater than 0")
        