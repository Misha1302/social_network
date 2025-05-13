from flask import *

from controllers.helpers.auth_service import AuthService
from controllers.helpers.statuses import Statuses
from data_objects.post import PostEncoder
from data_objects.user_login_data import UserLoginData
from database.user_service import UserService


def init_getter_controller(flask_app: Flask):
    @flask_app.post('/get_posts_to_show')
    def get_posts_to_show():
        posts = UserService().get_posts_by_topic(request.json['topic'])
        return [json.dumps(x, cls=PostEncoder) for x in posts]

    @flask_app.get('/get_topics')
    def get_topics():
        return UserService().get_topics()

    @flask_app.post('/get_is_right_login_and_password')
    def get_is_right_login_and_password():
        is_correct = AuthService().is_valid_user_login_data(
            UserLoginData(request.json['name'], request.json['password'])
        )

        if not is_correct:
            return "login or password are wrong", Statuses.BAD_REQUEST
        return "success", Statuses.OK
