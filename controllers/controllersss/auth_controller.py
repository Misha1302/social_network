from flask import Flask, request

from controllers.controllersss.app_controller import AppController
from controllers.helpers.statuses import Statuses
from data_objects.user_login_data import UserLoginData
from database.user_service import UserService


def init_auth_controller(flask_app: Flask):
    @flask_app.get('/get_auth_key')
    def get_auth_key():
        login_data = UserLoginData(request.json)
        found_users = UserService().get_users_with_this_name(login_data.name)
        if len(found_users) == 0:
            return f"No user found with that name ({login_data.name}", Statuses.NOT_FOUND
        if len(found_users) != 1:
            return f"There are {len(found_users)} users with this name. It's incorrect", Statuses.IM_A_TEAPOT

        found_user = found_users[0]
        if found_user.password != login_data.password:
            return f"Password mismatch", Statuses.BAD_REQUEST
        return f"{AppController().authService.get_auth_key(login_data)}", Statuses.OK
