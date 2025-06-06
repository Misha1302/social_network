from werkzeug.datastructures import FileStorage

from controllers.helpers.auth_service import AuthService
from data_objects.add_post_data import AddPostData
from data_objects.message import Message
from data_objects.root_password import RootPassword
from data_objects.user_login_data import UserLoginData
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
        if not AuthService().is_valid_user_login_data(UserLoginData(msg.auth_key, users1_id[0].name)):
            return False, f"Invalid auth key"
        return True, ""

    @classmethod
    def verify_image(cls, img: FileStorage) -> (bool, str):
        IMAGE_MAX_SIZE = 1 * 1024 * 1024

        size_in_bytes = len(img.stream.read())

        if size_in_bytes > IMAGE_MAX_SIZE:
            return False, f"Image must be lighter than {IMAGE_MAX_SIZE / 1024 / 1024} mb"
        return True, ""

    @classmethod
    def verify_password(cls, password: RootPassword) -> (bool, str):
        if not password.is_correct():
            return False, f"Password is incorrect"
        return True, ""

    @classmethod
    def verify_post_data(cls, add_post_data: AddPostData):
        login_data = UserLoginData(add_post_data.author_name, add_post_data.author_password)
        return AuthService.is_valid_user_login_data(login_data)
