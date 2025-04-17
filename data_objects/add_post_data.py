from typing import Any

from data_objects.post import Post


class AddPostData:
    def __init__(self, json_str: Any):
        self.author_name: str = json_str.get("author_name")
        self.author_password: str = json_str.get("author_password")
        self.post: Post = Post(json_str)
