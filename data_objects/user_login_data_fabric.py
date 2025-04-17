from typing import Any

from data_objects.user_login_data import UserLoginData


class UserLoginDataFabric:
    @staticmethod
    def new_user(json_str: Any):
        return UserLoginData(json_str.get("name"), json_str.get("password"))
