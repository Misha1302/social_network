from werkzeug.datastructures import FileStorage

from controllers.app_controller import AppController
from controllers.message import Message
from controllers.root_password import RootPassword
from database.user_service import UserService


class DataVerifier:
    @classmethod
    def verify_user_data(cls, user) -> (bool, str):
        if len(user.name) <= 2:
            return False, "User name must be longer than 2 characters"
        if len(user.password) <= 7:
            return False, "Password must be longer than 7 characters"
        if '@' not in user.email or '.' not in user.email:
            return False, "Email is incorrect"
        if not (0 <= user.get_years() <= 150):
            return False, "Invalid birth date"
        return True, ""

    @classmethod
    def verify_message(cls, msg: Message) -> (bool, str):
        users1_id = UserService().get_users_with_this_id(msg.user1_id)
        users2_id = UserService().get_users_with_this_id(msg.user2_id)
        if len(users1_id) == 0:
            return False, f"No user with ID={msg.user1_id}"
        if len(users2_id) == 0:
            return False, f"No user with ID={msg.user2_id}"
        # TODO: new ctors to never use [0][1] and use [0].name
        if not AppController().authService.is_valid_key(msg.auth_key, users1_id[0][1]):
            return False, f"Invalid auth key"
        return True, ""

    @classmethod
    def verify_image(cls, img: FileStorage) -> (bool, str):
        IMAGE_MAX_SIZE = 1 * 1024 * 1024

        size_in_bytes = len(img.stream.read())

        if size_in_bytes > IMAGE_MAX_SIZE:
            return False, f"Image must be lighter than {IMAGE_MAX_SIZE // 1024 // 1024} mb"
        return True, ""

    @classmethod
    def verify_password(cls, password: RootPassword) -> (bool, str):
        if not password.is_correct():
            return False, f"Password is incorrect"
        return True, ""
