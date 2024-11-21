import json
from typing import List

from database.user import User

json_encoder = json.JSONEncoder()


class JsonHelper:
    @classmethod
    def to_json(cls, value: List[User]):
        return json_encoder.encode([x.get_dict() for x in value])
