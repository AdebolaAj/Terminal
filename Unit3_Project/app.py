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

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from seed_library import seed_questions, seed_inventory
from flask_pymongo import PyMongo
from model import verify_user_answer, create_giftcard
from model import get_question_answer, add_question_answer_pair, redeem_user_giftcard
from model import addInventory, removeInventory, inquireInventory
import os

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:"+ os.environ.get('PASSWORD') +"@cluster0.wv93i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app)

# Comment out this create_collection method after you run the app for the first time
# mongo.db.create_collection('inventory')
# mongo.db.create_collection('log')
# mongo.db.create_collection('giftcards')
# mongo.db.create_collection('general_reviews')
# mongo.db.create_collection('item_reviews')
# mongo.db.create_collection('trivia_questions')


# -- Routes section --
# Seed Route
@app.route('/seed')
def seed():
    mongo.db.inventory.insert_many(seed_inventory)
    return redirect('/')

# INDEX Route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Beverages Route
@app.route('/beverages')
def beverages():
    return render_template('beverages.html')

# Sweet Food Route
@app.route('/sweet')
def sweet():
    return render_template('sweet.html')

# Savory Food Route
@app.route('/savory')
def savory():
    return render_template('savory.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Reviews Route
@app.route('/general_reviews', methods=['GET', 'POST'])
def general_reviews():
    if request.method == 'GET':
        return render_template('general_review.html')
    else:
        general_reviews_dict = {"Name": request.form['name'], "Phone Number": request.form['phoneNumber'], "email": request.form['email'], "Cleaniness Grade": request.form['cleaninessGrade'], "Server Grade": request.form["serverGrade"], "Treatment Grade": request.form["treatmentGrade"]}
    pass

@app.route('/item_reviews', methods=['GET', 'POST'])
def item_reviews():
    if request.method == 'GET':
        return render_template('general_review.html')
    else:
        item_reviews_dict = {"Name": request.form['name'], "Phone Number": request.form['phoneNumber'], "email": request.form['email'], "Cleaniness Grade": request.form['itemstasteGrade'], "Service Grade": request.form["serviceGrade"], "Items Satisfaction Grade": request.form["itemsSatisfactionGrade"]}
    pass
# Trivia Route
@app.route('/trivia', methods=['GET', 'POST'])
def trivia():
    if request.method == 'GET':
        return render_template('trivia.html')
    else:
        user_response = request.form['user_answer']
        correct_response = verify_user_answer(user_response)
        reward = None
        if correct_response:
            reward = create_giftcard() #reward is the giftcard code
        return render_template('giftcard_response.html', code=reward, correct=correct_response)

# Admin Route, would have links to /insert_question and /redeem_card and inventory management
@app.route('/admin/operations', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

# Add Questions Route
@app.route('/admin/add_question', methods=['GET', 'POST'])
def insert_question():
    if request.method == 'GET':
        return render_template('add_question.html')
    else:
        new_question = request.form['question']
        new_answer = request.form['answer']
        add_question_answer_pair(new_question, new_answer)
        return redirect('/admin/operations')

# Redeem Giftcard Route
@app.route('/admin/redeem_card', methods=['GET', 'POST'])
def redeem_user_card():
    if request.method == 'GET':
        return render_template('redeem_card.html')
    else:
        user_card_code = request.form['giftcode']
        card_state = redeem_user_giftcard(user_card_code) #value is None or the actual gift value
        correct = True
        if card_state is None:
            correct = False
        return render_template('redeem_response.html', message=card_state, correct=correct)

# Inventory
@app.route('/admin/inventory', methods=['GET', 'POST'])
def alter_inventory():
    
    if request.method == 'GET':
        return render_template('inventory.html')

    else:

        section = request.form['section']
        category = request.form['category']
        item = request.form['item']
        action = request.form['action']
        amount = request.form['amount']

        if action == "add":
            addInventory(section, category, item, amount)
            print(section, category, amount, item, amount)

        else:
            removeInventory(section, category, item, amount)

        return redirect('/admin/operations')
            



