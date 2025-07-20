# ## Phase 5 – Hands-On Tasks

# 1. Create signup form:
#     - Store users temporarily in a dictionary.
#     - Redirect to login after successful signup.

# 2. Create login form:
#     - Verify username and password.
#     - Use session to track logged-in user.

# 3. Create dashboard page:
#     - Only accessible when logged in.
#     - Display username dynamically.

# 4. Create logout functionality:
#     - Clear session and redirect to login.

# 5. Bonus:
#     - Style the forms with CSS.
#     - Display error messages for invalid login.

# 6. Super Bonus:
#     - Show flash messages (optional advanced concept).

from flask import Flask,request,render_template,session,redirect,url_for,flash
app = Flask(__name__)

app.secret_key="Admin1234"
users={}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/signup',methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/loginsubmit',methods=['POST'])
def loginsubmit():
    username=request.form['username']
    password=request.form['password']
    
    if username in users and users[username]==password:
        session['username']=username
        return redirect(url_for('dashboard'))
    flash("Login Failed")
    return redirect(url_for('signup'))


@app.route('/signupsubmit',methods=['POST'])
def signupsubmit():
    username=request.form['username']
    password=request.form['password']
    users[username]=password

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    username=session['username']
    return render_template('dashboard.html',username=username)
if __name__=='__main__':
    app.run(debug=True)