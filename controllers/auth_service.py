from uuid import uuid4

from controllers.user_login_data import UserLoginData


class AuthService:
    def __init__(self):
        self._keys = {}

    def get_auth_key(self, login_data: UserLoginData) -> str:
        if login_data.name not in self._keys:
            self._keys[login_data.name] = str(uuid4())
        return self._keys[login_data.name]

    def is_valid_key(self, key, user_name):
        return user_name in self._keys and self._keys.get(user_name) == key
