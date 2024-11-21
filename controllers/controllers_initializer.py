from flask import Flask

from controllers.controllersss import (auth_controller, root_controller, adding_controller)


def init_controllers(flask_app: Flask):
    adding_controller.init_adding_controller(flask_app)
    root_controller.init_root_controller(flask_app)
    auth_controller.init_auth_controller(flask_app)
