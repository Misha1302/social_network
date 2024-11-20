from typing import Any

import SECRETS


class RootPassword:
    def __init__(self, json_data: Any):
        self.password_text = json_data.get('password')

    def is_correct(self):
        return self.password_text == SECRETS.ROOT_PASSWORD
