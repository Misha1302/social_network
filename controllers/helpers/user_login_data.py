from typing import Any


class UserLoginData:
    def __init__(self, json_str: Any):
        self.name = json_str.get("name")
        self.password = json_str.get("password")
