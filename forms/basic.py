from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__) # create application

app.config['SECRET_KEY'] = 'mysecretkey' #secret to a string of our choosing (mysecretkey)

class InfoForm(FlaskForm): #we're inheriting FlaskForm here
#create our own form inheriting flaskform

    breed = StringField('What breed are you?') #attribute (breed)
    submit = SubmitField('Submit') #submit attribute, submit button

@app.route('/',methods=['GET','POST']) #allows us to pass in this form to the template
def index():
    breed = False #set breed variable to false, different from line 12. 12 is an attribute, 18 is just a variable
    form = InfoForm() #create an instance of our form
    if form.validate_on_submit(): #if form, we validate on submit
        breed = form.breed.data # we grab the breed from form.breed.data. this returns back the data that was submitted into line 12
        form.breed.data = '' #reset form.breed.data
    return render_template('index.html', form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)
