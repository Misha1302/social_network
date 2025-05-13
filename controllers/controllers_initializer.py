from flask import Flask

from controllers.controllers_initializers import (root_controller, adding_controller, getter_controller)


def init_controllers(flask_app: Flask):
    getter_controller.init_getter_controller(flask_app)
    adding_controller.init_adding_controller(flask_app)
    root_controller.init_root_controller(flask_app)
