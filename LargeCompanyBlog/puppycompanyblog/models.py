from puppycompanyblog import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True) #primary makes it a unique ID
    profile_image = db.Column(db.String(20), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # This connects BlogPosts to a User Author.
    posts = db.relationship('BlogPost', backref='author', lazy=True)
    '''
    #backref, adds a reference in the BlogPost model
    like in /blog_posts/views.py, line 42, we use # if blog_post.author != current_user:

    note: if we add uselist=False, we can create a one to one relationship.
    but since there will be several blogposts,
    we have a one to many relationship by leaving out uselist
    '''

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash,password)

    def __repr__(self): #gives you the string representation of the object, good for when debugging.
        return f"UserName: {self.username}"

class BlogPost(db.Model):
    # Setup the relationship to the User table
    users = db.relationship(User)

    # Model for the Blog Posts on Website
    id = db.Column(db.Integer, primary_key=True)
    # Notice how we connect the BlogPost to a particular author
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) #directly connected the blogpost to the user, using ForeignKey
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id =user_id


    def __repr__(self):
        return f"Post Id: {self.id} --- Date: {self.date} --- Title: {self.title}"

'''
models.py is setting up a table in our database
line 23 is to manually overwrite the tablename - unsure what default it. can't find any documentation on it
here we have 2 classes. defining it's relationship and columns.
'''
