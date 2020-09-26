from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import json
#-----------------------------------------------------------------
app = Flask(__name__)
with open('info.json','r') as c:
    info = json.load(c)["Information"]

app.config['SQLALCHEMY_DATABASE_URI'] = info["Production_Server"] 
db = SQLAlchemy(app)   
#-----------------------------------------------------------------
class Feedback(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100),  nullable=False )
    Email = db.Column(db.String(100),  nullable=False)
    Message = db.Column(db.String(1000),  nullable=False)
#-----------------------------------------------------------------  
class Subscribers(db.Model):
    Email = db.Column(db.String(100),  primary_key=True)
#-----------------------------------------------------------------   
@app.route('/', methods=['GET','POST'])
def HomePage():
    if(request.method == 'POST'):
        email = request.form.get('email')
        en = Subscribers(Email = email)
        db.session.add(en)
        db.session.commit()
    return render_template('index.html')

@app.route('/index.html', methods=['GET','POST'])
def Home_back():
    if(request.method == 'POST'):
        email = request.form.get('email')
        en = Subscribers(Email = email)
        db.session.add(en)
        db.session.commit()

    return render_template('index.html')
#----------------------------------------------------------------
@app.route('/Distress.html', methods=['GET','POST'])
def registerDistress():
    
        
    if(request.method == 'POST'):
        first_name = request.form.get('Fname')
        last_name = request.form.get('Lname')
        phone_number = request.form.get('Phno')
        city = request.form.get('City')
        state = request.form.get('State')
        pin_code = request.form.get('Zip')
        msg = request.form.get('Messgae')
        print(state)
        # en = Subscribers(Email = email)
        # db.session.add(en)
        # db.session.commit()
    return render_template('Distress.html')
#-----------------------------------------------------------------
@app.route('/Contact.html' ,  methods=['GET','POST'])
def Develouper_contact():
    if(request.method == 'POST'):
        """ Add entry to the database """
        name = request.form.get('Name')
        email = request.form.get('Email')
        message = request.form.get('Message')    
        entry = Feedback(Name = name , Email = email , Message = message)
        db.session.add(entry)
        db.session.commit()    
        
    return render_template('Contact.html')    
#----------------------------------------------------------------- 
@app.route('/selfAssess.html' , methods=['GET','POST'])
def Assess():
    if(request.method == 'POST'):
        problems=[]
        gender = request.form.get('Gender')
        name = request.form.get('pname')
        age = request.form.get('age')
        email = request.form.get('e')
        problems.append(request.form.get('headace'))
        problems.append(request.form.get('Fever'))
        problems.append(request.form.get('Cough'))
        problems.append(request.form.get('Diarrhea'))
        problems.append(request.form.get('Breathing Difficulty'))
        problems.append(request.form.get('Chest Pressure'))
        problems.append(request.form.get('Nasal'))
        problems.append(request.form.get('Sweating'))
        problems.append(request.form.get('Skin'))
        problems.append(request.form.get('Muscle'))
        problems.append(request.form.get('Nausea'))
        problems.append(request.form.get('Abdominal'))
        problems.append(request.form.get('Itchy Eyes'))
        problems.append(request.form.get('Vomiting'))
        problems.append(request.form.get('Heartburn'))
        problems.append(request.form.get('Wheezing'))
        problems.append(request.form.get('Throat'))
        problems.append(request.form.get('Sleeping'))
        problems.append(request.form.get('Tiredness'))
        check_for_disease(name,email,problems)

    return render_template('selfAssess.html')
def check_for_disease(name,email,dis):
    pd.read_csv("/static/Dataset/Dataset.csv")
    pd.head()
app.run(debug = True)    