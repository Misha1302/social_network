from typing import List, Any

from data_objects.message import Message
from data_objects.post import Post
from data_objects.user import User
from database.images_service import ImagesService
from database.sqlite_cursor_provider import SqliteCursorProvider


def to_users(collection: List[Any]):
    return [User(x) for x in collection]


def to_posts(collection: List[Any]):
    return [Post(x) for x in collection]


# TODO: invulnerable to sql injections
class UserService:
    def add_user(self, user: User):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(
                f"INSERT INTO users VALUES ('{user.user_id}', '{user.name}', '{user.password}', '{user.email}', '{user.birth_date}')")

    def get_all_users(self):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute("SELECT * FROM users")
            return to_users(cursor.fetchall())

    def get_users_with_this_name(self, name):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(f"SELECT * FROM users WHERE user_name = '{name}'")
            return to_users(cursor.fetchall())

    def get_users_with_this_id(self, user_id):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
            return to_users(cursor.fetchall())

    def add_message(self, msg: Message):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(
                f"INSERT INTO messages VALUES ('{msg.msg_id}', '{msg.user1_id}', '{msg.user2_id}', '{msg.msg_text}')")

    def add_post(self, post: Post):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(
                f"INSERT INTO posts VALUES ('{post.post_id}', '{post.post_text}', '{post.topic}')")

    def add_image(self, img):
        return ImagesService().add_image(img)

    def get_posts_by_topic(self, topic: str):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(f"SELECT * FROM posts WHERE topic = {topic}")
            return to_posts(cursor.fetchall())
