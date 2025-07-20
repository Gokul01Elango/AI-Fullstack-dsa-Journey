from flask import Flask,request,render_template,url_for,redirect,flash,session

app = Flask(__name__)

app.secret_key="secretkey"
# Login page render
users={}
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

#SignUp Page Render

@app.route('/signup',methods=['GET'])
def signup():
    return render_template('signup.html')

#submit method

@app.route('/loginsubmit',methods=['post'])
def loginsubmit():
    username=request.form['username']
    password=request.form['password']
    session[username]=username
    if username in users and users[username]==password:
        session['username']=username
        return render_template('Dashboard.html',username=username)
    flash("Login Failed")
    return redirect(url_for('login'))
    
    
# signup submit logic

@app.route('/signupsubmit',methods=['post'])
def signupsubmit():
    username=request.form['username']
    password=request.form['password']
    users[username]=password
    return redirect(url_for('login'))

# logout logic

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard',methods=['Get'])
def dashboard():
    if users in session:
        return render_template('dashboard.html')
    
if __name__=='__main__':
    app.run(debug=True)
