from flask import Flask, request

from controllers.root_password import RootPassword
from controllers.statuses import Statuses
from database.data_verifier import DataVerifier
from database.user_service import UserService


def init_root_controller(flask_app: Flask):
    @flask_app.get('/get_all_users')
    def get_all_users():
        password = RootPassword(request.json)

        is_correct, error = DataVerifier.verify_password(password)
        if not is_correct:
            return error, Statuses.BAD_REQUEST

        return UserService().get_all_users(), Statuses.OK
