from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Jose"
    letters = list(name)
    pup_dict = {'pup_name':'Sammy'}

    mylist = [1,2,3,4,5]

    puppies = ['Fluffy','Rufus','Spike']

    #code code
    userloggedin = True
    return render_template('basic.html', name=name, letters=letters,pup=pup_dict, mylist=mylist, puppies=puppies, userloggedin=userloggedin)

if __name__ == '__main__':
    app.run(debug=True)
