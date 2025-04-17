from data_objects.user import User
from data_objects.user_login_data import UserLoginData
from database.user_service import UserService


class AuthService:
    @classmethod
    def is_valid_user_user(cls, user: User) -> bool:
        return cls.is_valid_user_login_data(UserLoginData(user.name, user.password))

    @classmethod
    def is_valid_user_login_data(cls, login_data: UserLoginData) -> bool:
        found_users = UserService().get_users_with_this_name(login_data.name)
        return len(found_users) == 1 and found_users[0].password == login_data.password
