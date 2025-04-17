from flask import *

from controllers.helpers.auth_service import AuthService
from controllers.helpers.statuses import Statuses
from data_objects.user_login_data import UserLoginData
from database.user_service import UserService


def init_auth_controller(flask_app: Flask):
    @flask_app.get('/get_posts_to_show')
    def get_posts_to_show(topic: str):
        return UserService().get_posts_by_topic(topic)

    @flask_app.get('/get_is_right_login_and_password')
    def get_is_right_login_and_password():
        is_correct, error = AuthService() \
            .is_valid_user_login_data(UserLoginData(request.json['name'], request.json['password']))

        if not is_correct:
            return error, Statuses.BAD_REQUEST
        return "success", Statuses.OK
