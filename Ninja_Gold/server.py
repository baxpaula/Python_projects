
import random
from flask import Flask,render_template, request, redirect, session 


app = Flask(__name__)
app.secret_key = 'Keeping up with coding'

@app.route('/')          
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['my_activity'] = ''
    return render_template('index.html') 

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'Farm':
        ran_num = random.randint(10,20)
        session['gold'] += ran_num
        session['my_activity']+= f"<p style = 'color: green'> Earned {ran_num} golds from the farm!</p>"
        
    elif request.form['building'] == 'Cave':
            ran_numCave = random.randint(5,10)
            session['gold'] += ran_numCave
            session['my_activity']+= f"<p style = 'color: green'>Earned {ran_numCave} golds from the cave!</p>"
            
    elif request.form['building'] == 'House':
            ran_numHouse = random.randint(2,5)
            session['gold'] += ran_numHouse
            session['my_activity']+= f"<p style = 'color: green'>Earned {ran_numHouse} golds from the House!</p>"
            
    elif request.form['building'] == 'Casino':
        ran_numCasino = random.randint(-50,50)
        session['gold'] += ran_numCasino 
        if ran_numCasino < 0:
            session['my_activity']+= f"<p style = 'color: red'>Entered a Casino and lost{ran_numCasino} golds ...Ouch...</p>"
            
        else:
            session['my_activity']+= f"<p style = 'color: green'> Earned {ran_numCasino} golds from the Casino</p>"
            
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)   


