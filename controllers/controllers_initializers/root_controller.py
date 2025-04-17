from flask import Flask, request

from controllers.helpers.json_helper import JsonHelper
from controllers.helpers.statuses import Statuses
from data_objects.root_password import RootPassword
from database.data_verifier import DataVerifier
from database.user_service import UserService


def init_root_controller(flask_app: Flask):
    @flask_app.get('/get_all_users')
    def get_all_users():
        password = RootPassword(request.json)

        is_correct, error = DataVerifier.verify_password(password)
        if not is_correct:
            return error, Statuses.BAD_REQUEST

        return JsonHelper.to_json(UserService().get_all_users()), Statuses.OK
