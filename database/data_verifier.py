from werkzeug.datastructures import FileStorage

from controllers.message import Message
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
        if len(UserService().get_users_with_this_id(msg.user1_id)) == 0:
            return False, f"No user with ID={msg.user1_id}"
        if len(UserService().get_users_with_this_id(msg.user2_id)) == 0:
            return False, f"No user with ID={msg.user2_id}"
        return True, ""

    @classmethod
    def verify_image(cls, img: FileStorage) -> (bool, str):
        IMAGE_MAX_SIZE = 1 * 1024 * 1024

        size_in_bytes = len(img.stream.read())

        if size_in_bytes > IMAGE_MAX_SIZE:
            return False, f"Image must be lighter than {IMAGE_MAX_SIZE // 1024 // 1024} mb"
        return True, ""
