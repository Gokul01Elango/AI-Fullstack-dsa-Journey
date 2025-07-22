from flask import Flask,Blueprint,request,jsonify,render_template
from storage import users, sessions

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/')
def home():
    return "Home Page rendered Successfully"

# Login route
@auth_bp.route('/api/login')
def login():
    return render_template('login.html')

# Login submit route

@auth_bp.route('/api/loginsubmit',methods=['POST','GET'])
def loginsubmit():
    username=request.form['username']
    password=request.form['password']
    
    # Checking existing users
    if username in users and users[username]==password: 
        sessions[username]
        return f"{username} Logged in Success"
    
    
    return "incorrect Credentials"

# ----------------- # ---------------- # ------------------- # ----------------- # -------

# User Registration

@auth_bp.route('/api/signup')
def signup():
    return render_template('signup.html')

@auth_bp.route('/api/signupsubmit',methods=['POST','GET'])
def register():
    username=request.form['username']
    password=request.form['password']
    if username not in users:
        users[username]=password
        return "register success"
    else :
        return "username already Exist"
    

# Session Handling 

