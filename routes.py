from flask import Flask, render_template, request, url_for, redirect, jsonify
from models import db, User
from forms import AddUserForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Swagger123!@localhost/homework_users'
db.init_app(app)
app.secret_key = 'dbd3'

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', title='Home', users=users)


if __name__ == "__main__":
    app.run()

