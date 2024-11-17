from flask import *

from database.user_service import UserService


def init_controller(flask_app: Flask):
    @flask_app.post('/add_user')
    def add_new_user():
        UserService().add_user(request.json.get('name'), request.json.get('birth_date'))
        return 'User added!'

    @flask_app.get('/get_all_users')
    def get_all_users():
        return UserService().get_all_users()
