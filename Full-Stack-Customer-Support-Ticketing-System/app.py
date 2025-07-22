from flask import Flask
from routes.auth import auth_bp
from routes.tickets import tickets_bp
from storage import sessions,users
app=Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(tickets_bp)

if __name__=='__main__':
    app.run(debug=True)