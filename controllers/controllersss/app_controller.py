from controllers.helpers.auth_service import AuthService
from controllers.helpers.singleton import Singleton


class AppController(metaclass=Singleton):
    def __init__(self):
        self.authService: AuthService = AuthService()
