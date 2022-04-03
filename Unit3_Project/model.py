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
from generalreview import *
from itemreview import *
import pymongo
import os 

client = pymongo.MongoClient("mongodb+srv://admin:"+ os.environ.get('PASSWORD') +"@cluster0.wv93i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.myFirstDatabase

def create_giftcard():
    card = Giftcard.create_new()
    giftcardsDB = db.giftcards
    giftcardsDB.insert_one(card.to_document())
    return card.gift_code

def redeem_user_giftcard(giftcode):
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
    triviaDB = db.trivia_questions
    usable = triviaDB.find_one({"used":False})
    triviaDB.update_one({"question": usable["question"]}, {"$set": {"used": True}})
    return usable["question"], usable["answer"]

question, answer = get_question_answer()

def verify_user_answer(user_answer):
    return user_answer.lower() == answer.lower()

def add_question_answer_pair(question, answer):
    triviaDB = db.trivia_questions
    new_question_answer_pair = {"question": question, "answer": answer, "used": False}
    triviaDB.insert_one(new_question_answer_pair)

def inquireInventory(section, category, item, amount):

    inventory = db.inventory 
    item_info = inventory.find_one({'section': section, 'category': category, 'item': item})
    
    return item_info['amount']


def addInventory(section, category, item, amount):

    inventory = db.inventory 
    item_info = inventory.find_one({'section': section, 'category': category, 'item': item})
    item_instance = Inventory.from_document(item_info)
    item_instance.AddAmount(amount)
    inventory.update_one({'section': section, 'category': category, 'item': item }, {'$set': {'amount': item_instance.amount}})
    return f"The new amount for {section} -> {category} -> {item} is {item_instance.amount}"


def removeInventory(section, category, item, amount):

    inventory = db.inventory 
    item_info = inventory.find_one({'section': section, 'category': category, 'item': item})
    item_instance = Inventory.from_document(item_info)
    
    if item_instance.amount >= amount:
        item_instance.RemoveAmount(amount)
        inventory.update_one({'section': section, 'category': category, 'item': item}, {'$set': {'amount': item_instance.amount}})
        return f"The new amount for {section} -> {category} -> {item} is {item_instance.amount}"        

    else:

        return f"{section} -> {category} -> {item} has less than {amount} in stock"

def create_general_review(new_review):
    general_reviewsDB = db.general_reviews
    new_review = GeneralReview.from_form(new_review)
    new_review_doc = new_review.to_document()
    general_reviewsDB.insert_one(new_review_doc)
    return new_review_doc


def create_item_review(new_review):
    item_reviewsDB = db.item_reviews
    new_review = ItemReview.from_form(new_review)
    new_review_doc = new_review.to_document()
    item_reviewsDB.insert_one(new_review_doc)
    return new_review_doc
    