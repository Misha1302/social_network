from flask import *

from controllers.message import Message
from controllers.statuses import Statuses
from database.data_verifier import DataVerifier
from database.user import User
from database.user_service import UserService


def init_controller(flask_app: Flask):
    @flask_app.post('/add_user')
    def add_new_user():
        user = User(request.json)

        is_correct, error = DataVerifier.verify_user_data(user)
        if not is_correct:
            return error, Statuses.BAD_REQUEST

        service = UserService()

        if service.get_users_with_this_name(user.name):
            return f'User with name {user.name} already exists', Statuses.BAD_REQUEST

        service.add_user(user)
        return f'User with name {user.name} was added', Statuses.CREATED

    @flask_app.post('/add_message')
    def add_message():
        msg = Message(request.json)

        is_correct, error = DataVerifier.verify_message(msg)
        if not is_correct:
            return error, Statuses.BAD_REQUEST

        UserService().add_message(msg)
        return f'Message created', Statuses.CREATED

    @flask_app.get('/get_all_users')
    def get_all_users():
        return UserService().get_all_users(), Statuses.OK
