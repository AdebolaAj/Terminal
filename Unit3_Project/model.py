# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from giftcards import *
from inventory import *
import pymongo
import os 

client = pymongo.MongoClient("mongodb+srv://admin:"+ os.environ.get('PASSWORD') +"@cluster0.wv93i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.myFirstDatabase

def create_giftcard():
    """Creates a Giftcard object instance.

    Returns:
        str: The giftcode associated with a Giftcard object.
    """
    card = Giftcard.create_new()
    giftcardsDB = db.giftcards
    giftcardsDB.insert_one(card.to_document())
    return card.gift_code

def redeem_user_giftcard(giftcode):
    """Redeems a Giftcard object for its value.

    Args:
        giftcode (str): The giftcode for the Giftcard object to be redeemed.
    Returns:
        str: The value associated with a giftcard object. Returns None if the card has been previously redeemed.
    """
    if not Giftcard.authenticate(giftcode):
        return None
    giftcardsDB = db.giftcards
    card_doc = giftcardsDB.find_one({"giftcode": giftcode})
    if not card_doc:
        return None
    giftcard_obj = Giftcard.from_document(card_doc)    
    value = giftcard_obj.redeem() 
    update = giftcard_obj.to_document()
    giftcardsDB.update_one({"giftcode": update["giftcode"]}, {"$set": {"redeem_state": update["redeem_state"]}})
    return value

def get_question_answer():
    """Gets a trivia question-answer pair for day from the database.

    Returns:
        str: The selected question.
        str: The answer associated with the selected question.
    """
    triviaDB = db.trivia_questions
    usable = triviaDB.find_one({"used":False})
    triviaDB.update_one({"question": usable["question"]}, {"$set": {"used": True}})
    return usable["question"], usable["answer"]

question, answer = get_question_answer()

def verify_user_answer(user_answer):
    """Checks that a user's answer is the correct answer to the trivia question.

    Args:
        user_answer (str): The user's attempt answer to the daily trivia question.
    Returns:
        bool: Indicates whether user got the answer right or wrong.
    """
    return user_answer.lower() == answer.lower()

def add_question_answer_pair(question, answer):
    """Adds a new question-answer pair to the database.

    Args:
        question (str): The new question.
        answer (str): The answer associated with the new question.
    """
    triviaDB = db.trivia_questions
    new_question_answer_pair = {"question": question, "answer": answer, "used": False}
    triviaDB.insert_one(new_question_answer_pair)

def inquireInventory(section, category, item, amount):

    inventory = db.inventory 
    item_info = inventory.find_one({'section': section, 'category': category, 'item': item})
    
    return item_info['amount']


def addInventory(section, category, item, amount):
    amount = int(amount)
    inventory = db.inventory 
    item_info = inventory.find_one({'section': section, 'category': category, 'item': item})
    item_instance = Inventory.from_document(item_info)
    item_instance.AddAmount(amount)
    inventory.update_one({'section': section, 'category': category, 'item': item }, {'$set': {'amount': item_instance.amount}})
    return f"The new amount for {section} -> {category} -> {item} is {item_instance.amount}"


def removeInventory(section, category, item, amount):

    amount = int(amount)
    inventory = db.inventory 
    item_info = inventory.find_one({'section': section, 'category': category, 'item': item})
    item_instance = Inventory.from_document(item_info)
    
    if item_instance.amount >= amount:
        item_instance.RemoveAmount(amount)
        inventory.update_one({'section': section, 'category': category, 'item': item}, {'$set': {'amount': item_instance.amount}})
        return f"The new amount for {section} -> {category} -> {item} is {item_instance.amount}"        

    else:

        return f"{section} -> {category} -> {item} has less than {amount} in stock"
