import uuid
from typing import Any


class Message:
    def __init__(self, json_str: Any):
        self.user1_id = json_str.get("user1_id")
        self.user2_id = json_str.get("user2_id")
        self.msg_text = json_str.get("msg_text")

        self.msg_id = uuid.uuid4()
