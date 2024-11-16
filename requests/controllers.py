from Db.UserService import UserService
from app import *


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.post('/add_user')
def add_new_user():
    UserService().add_user(request.json.get('name'), request.json.get('birth_date'))
    return 'User added!'


@app.get('/get_all_users')
def get_all_users():
    return UserService().get_all_users()


def useless():
    return None
