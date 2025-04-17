import uuid
from typing import Any


class Post:
    def __init__(self, json_str: Any):
        self.post_id: uuid.uuid4 = uuid.uuid4()
        self.post_text: str = json_str.get("post_text")
        self.topic: str = json_str.get("topic")
