# ## 📄 Phase 1 – Practice Tasks

# 1. Create a Flask project folder with the correct structure.
# 2. Set up `app.py` with a basic route `/` and render an HTML page.
# 3. Create a basic `index.html` in templates folder.
# 4. Link and apply CSS using `static/style.css`.
# 5. Change page content dynamically using Jinja2:
#     - Pass a list of skills from Python to your HTML.
#     - Display the skills using a for-loop inside HTML.

# Example: skills = ['Python', 'Flask', 'HTML']

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/skills')
def skills():
    skills=["RAG","AI","Python","LLM"]
    return render_template('index.html',skills=skills)





## Phase 2 – Hands-On Practice

# 1. Create a new form page:
#     - Fields: Name, Email, Feedback
#     - Submit via POST method.

# 2. On submission:
#     - Show a confirmation page displaying all submitted data.

# 3. Bonus Task:
#     - Create a contact form page (Name, Subject, Message).
#     - Store submitted messages in a list (temporarily) on server-side.
#     - Display all messages on a separate page (`/messages`).


@app.route('/submit',methods=['POST'])

def submit():
    username=request.form['username']
    email=request.form['email']
    feedback=request.form['feedback']
    return render_template('result.html',username=username,email=email,feedback=feedback)



# ## Phase 3 – Hands-On Tasks

# 1. Style your form page (`form.html`):
#     - Input boxes and button should look professional.
#     - Use background colors, borders, hover effects.

# 2. Style result page (`result.html`):
#     - Make the greeting message larger and centered.

# 3. Add simple JS interaction:
#     - Alert user when they click submit.
#     - Change button color after clicking (using JS).

# 4. BONUS:
#     - Add simple fade-in animation using CSS for the message display.

## Phase 4 – Practice Tasks

# 1. Create `base.html` with:
#    - Navigation bar
#    - Shared CSS styling
#    - Jinja2 content block

# 2. Create multi-page website with:
#    - Home page
#    - About page
#    - Contact page

# 3. Use Jinja inheritance (`{% extends %}`) in all pages.

# 4. Bonus:
#    - Style the navigation bar (highlight current page if possible).
#    - Add a footer to `base.html`.

# 5. Super Bonus:
#    - Create a separate page (e.g. `/projects`) and link it via navigation.

@app.route('/base')
def home():
    return render_template('base.html')


if __name__=='__main__':
    app.run(debug=True)