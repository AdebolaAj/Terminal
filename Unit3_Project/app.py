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
from seed_library import seed_books
from flask_pymongo import PyMongo
from model import genres

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "<mongo_uri_here>"

#Initialize PyMongo
mongo = PyMongo(app)

# Comment out this create_collection method after you run the app for the first time
# mongo.db.create_collection('library')

# -- Routes section --
# INDEX Route
@app.route('/')
@app.route('/index')
def index():
    books = []
    return render_template('index.html', books = books)


# NEW BOOK Route
@app.route('/new')
def new_book():
    return render_template('new_book.html', genres = genres)

