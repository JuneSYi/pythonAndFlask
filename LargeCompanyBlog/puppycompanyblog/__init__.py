from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

############################
####### DATABASE SETUP
#############
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


######################
########### LOGIN CONFIGURATIONS
############################
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'




###################

from puppycompanyblog.core.views import core
from puppycompanyblog.users.views import users
from puppycompanyblog.blog_posts.views import blog_posts
from puppycompanyblog.error_pages.handlers import error_pages


app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)

'''
assign app to Flask object.
flask constructor takes the name of current module(__name__) as argument

setup the database
establish base directory path (we use os package)
create database objective (assigned to db)
migrate it (SQLAlchemy Migrate provides a way to deal with database schema changes in SQLAlchemy projects.)

setup login configuration
setup blueprint model for each subdirectory (with .py files)

additional details on blueprint:
Each Flask Blueprint is an object that works very similarly to a Flask application.
They both can have resources, such as static files, templates, and views that are associated with routes.

However, a Flask Blueprint is not actually an application. It needs to be registered in an application before you can run it.
When you register a Flask Blueprint in an application, you’re actually extending the application with the contents of the Blueprint.

This is the key concept behind any Flask Blueprint. They record operations to be executed later when you register them on an application.
For example, when you associate a view to a route in a Flask Blueprint, it records this association to be made later in the application when the Blueprint is registered.
'''
