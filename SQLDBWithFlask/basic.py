import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #pip install Flask-Migrate


basedir = os.path.abspath(os.path.dirname(__file__))
# os library (line 1)
# __file__ = when a module is loaded in python, this file variable is built in, and it's set in to the name of the actual __file__
# in this case __file__ = basic.py
# then we want to ge tthe actual directory name for where the file is
# os.path.dirname is doing this (line 10) e.g. /pythonAndFlaskBootcamp/SQLDBWithFlask/
#then we want the absolute path (abspath) e.g. c://User/name/Desktop/
print(basedir)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
#this sets up the db location and where it's going to be setup
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# we don't want to have to track every single modfiication in our db, by default it does, so we make it False

db = SQLAlchemy(app)
# we call sqlalchemy and pass in our app
#now we've set up our SQLite DB. specifically lines 6-22

Migrate(app,db) #flask migrate, connects the app to db

###############################################
class Puppy(db.Model):

    # this is how you manually overwrite the tablename, otherwise, sqlalchemy will automatically take your class name and adds an S to it
    __tablename__ = 'puppies'

    #columns for the table
    id = db.Column(db.Integer,primary_key=True)
    # within our puppy class, we have an attribute called id, we're setting id equal to a column inside the table
    # the actual colun type is set to Integer, primary key = unique identifier for the rows
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age,breed):
        self.breed = breed
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old"
