from controllers.message import Message
from database.images_service import ImagesService
from database.sqlite_cursor_provider import SqliteCursorProvider
from database.user import User


# TODO: invulnerable to sql injections
class UserService:
    def add_user(self, user: User):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(
                f"INSERT INTO users VALUES ('{user.user_id}', '{user.name}', '{user.password}', '{user.email}', '{user.birth_date}')")

    def get_all_users(self):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()

    def get_users_with_this_name(self, name):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(f"SELECT * FROM users WHERE user_name = '{name}'")
            return cursor.fetchall()

    def get_users_with_this_id(self, id):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(f"SELECT * FROM users WHERE user_id = '{id}'")
            return cursor.fetchall()

    def add_message(self, msg: Message):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(
                f"INSERT INTO messages VALUES ('{msg.msg_id}', '{msg.user1_id}', '{msg.user2_id}', '{msg.msg_text}')")

    def add_image(self, img):
        return ImagesService().add_image(img)
