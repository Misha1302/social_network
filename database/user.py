from datetime import datetime
from typing import Any


class User:
    def __init__(self, json_data: Any):
        self.name = json_data.get('name')
        self.password = json_data.get('password')
        self.birth_date = json_data.get('birth_date')
        self.email = json_data.get('email')

    def get_years(self):
        return datetime.now().year - datetime(*map(int, self.birth_date.split())).year
