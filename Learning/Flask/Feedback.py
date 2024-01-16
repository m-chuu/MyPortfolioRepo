# This is because our books are currently stored in the List all_books, 
# this variable gets re-initialised when we re-run main.py and all the data inside is lost.
# If this happened to our user's data, they would not have much faith in our website.
# In order to fix this, we need to learn about data persistence and how to work with databases in Flask applications

# So a cursor is also known as the mouse or pointer. 
# If we were working in Excel or Google Sheet, 
# we would be using the cursor to add rows of data or edit/delete data, 
# we also need a cursor to modify our SQLite database.

#  All actions in SQLite databases are expressed as SQL (Structured Query Language) commands.
# There are quite a few SQL commands. But don't worry, you don't have to memorise them.
# https://www.codecademy.com/article/sql-commands

# It would be much better if we could just write Python code and get the compiler to help us spot typos and errors in our code. 
# That's why SQLAlchemy was created.

# SQLAlchemy is defined as an ORM (Object Relational Mapping) library. 
# This means that it's able to map the relationships in the database into Objects. 
# Fields become Object properties. Tables can be defined as separate Classes and each row of data is a new Object.
# This will make more sense after we write some code and see how we can create a Database/Table/Row of data using SQLAlchemy.

# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/
# from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, url_for,json


app = Flask(__name__)

# ##CREATE DATABASE
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///feedbacks-collection.db"

# # Create the extension
# db = SQLAlchemy()
# # Initialise the app with the extension
# db.init_app(app)

# ##CREATE TABLE
# class Feedbacks(db.Model):
#     User_ID = db.Column(db.Integer, primary_key=True)
#     Satisfaction = db.Column(db.String(250), nullable=False)
#     Usability = db.Column(db.String(250), nullable=False)
#     Content_quality = db.Column(db.String(250), nullable=False)

#     # Optional: this will allow each book object to be identified by its title when printed.
#     def __repr__(self):
#         return f'<Feedbacks {self.title}>'

# # Create table schema in the database. Requires application context.
# with app.app_context():
#     db.create_all()

# # CREATE RECORD
# with app.app_context():
#     new_feedback = Feedbacks(User_ID=1, Satisfaction="Perfect", Usability="Perfect", Content_quality="Perfect")
#     db.session.add(new_feedback)
#     db.session.commit()

def init_db():
    db = sqlite3.connect("feedbacks-database.db")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS feedbacks (
        User_ID INTEGER PRIMARY KEY,
        Satisfaction TEXT NOT NULL,
        Usability TEXT NOT NULL,
        Content_quality TEXT NOT NULL
    )""")

    try:
        cursor.execute("INSERT INTO feedbacks (User_ID, Satisfaction, Usability, Content_quality) VALUES (13, 'Perfect', 'Perfect', 'Normal')")
        db.commit()
    except sqlite3.IntegrityError:
        print("Record already exists.")
 
    db.close()

all_feedbacks = []

@app.route('/')
def index():
    return "Welcome to the Feedback Form"

@app.route('/feedback')
def feedback():
    return render_template('feedback_form.html', feedbacks=all_feedbacks)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    user_id = request.form["user-id"]
    overall_satisfaction = request.form["overall-satisfaction"]
    usability = request.form["usability"]
    content_quality = request.form["content-quality"]

    feedback_data = {
        "user_id": user_id,
        "overall_satisfaction": overall_satisfaction,
        "usability": usability,
        "content_quality": content_quality
    }

    all_feedbacks.append(feedback_data)
    print(feedback_data)

    with open('Learning/Flask/feedback_data.txt', 'a') as file:
        file.write(json.dumps(feedback_data) + '\n')

    return redirect(url_for('feedback'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

