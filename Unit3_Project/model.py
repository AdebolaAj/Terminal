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

client = pymongo.MongoClient("mongodb+srv://admin:"+ os.environ.get('PASSWORD') +"@cluster0.wv93i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.myFirstDatabase

def create_giftcard():
    card = Giftcard()
    return card.gift_code

def redeem_user_giftcard(giftcode):
    return Giftcard.redeem(giftcode)

def get_question_answer():
    triviaDB = db.trivia_questions
    usable = triviaDB.find_one({"used":False})
    triviaDB.update_one({"question": usable["question"]}, {"$set": {"used": True}})
    return usable["question"], usable["answer"]

question, answer = get_question_answer()

def verify_user_answer(user_answer):
    return user_answer.lower() == answer.lower()

def add_question_answer_pair(question, answer):
    #adds a new trivia question-answer pair to the database collection
    #admin/operation function
    triviaDB = db.trivia_questions
    new_question_answer_pair = {"question": question, "answer": answer, "used": False}
    triviaDB.insert_one(new_question_answer_pair)