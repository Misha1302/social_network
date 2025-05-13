import json
import uuid
from typing import Any


class Post:
    def __init__(self, json_str: Any):
        self.post_id: uuid.uuid4 = uuid.uuid4()
        if type(json_str) != tuple:
            self.post_text: str = json_str.get("post_text")
            self.topic: str = json_str.get("topic")
        else:
            self.post_text: str = json_str[1]
            self.topic: str = json_str[2]

class PostEncoder(json.JSONEncoder):
    def encode(self, obj):
        if isinstance(obj, Post):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)