import Database
from app import *


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add_user/<name>/<birth_date>')
def add_new_user(name, birth_date):
    with Database.Database() as db:
        db.add_user(name, birth_date)
    return 'User added!'


@app.route('/get_all_users')
def get_all_users():
    with Database.Database() as db:
        return db._execute("SELECT * FROM users")
