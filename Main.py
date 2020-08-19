from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def HomePage():
    return render_template('index.html')

@app.route('/Contact.html')
def Develouper_contact():
    return render_template('Contact.html')    

@app.route('/index.html')
def Home_back():
    return render_template('index.html')

app.run(debug = True)    