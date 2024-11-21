from datetime import datetime
from json import JSONEncoder
from typing import Any, Tuple
from uuid import uuid4


class User(JSONEncoder):
    def __init__(self, json_data: Any):
        super().__init__()

        self.user_id, self.name, self.password, self.birth_date, self.email = (
            self.extract_tuple(json_data) if isinstance(json_data, Tuple) else self.extract_json(json_data)
        )

    def get_years(self):
        return datetime.now().year - datetime(*map(int, self.birth_date.split())).year

    @classmethod
    def extract_json(cls, json_data: Any) -> Tuple[Any, Any, Any, Any, Any]:
        return (
            uuid4() if 'user_id' not in json_data else json_data['user_id'],
            json_data.get('name'),
            '' if 'password' not in json_data else json_data.get('password'),
            '' if 'birth_date' not in json_data else json_data.get('birth_date'),
            '' if 'email' not in json_data else json_data.get('email')
        )

    @classmethod
    def extract_tuple(cls, json_data: Any) -> Tuple[Any, Any, Any, Any, Any]:
        return (
            json_data[0],
            json_data[1],
            json_data[2],
            json_data[3],
            json_data[4]
        )

    def get_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'password': self.password,
            'birth_date': self.birth_date,
            'email': self.email
        }
