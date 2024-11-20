from flask import Flask

import controllers.adding_controller
import controllers.root_controller
import controllers.auth_controller


def init_controllers(flask_app: Flask):
    controllers.adding_controller.init_adding_controller(flask_app)
    controllers.root_controller.init_root_controller(flask_app)
    controllers.auth_controller.init_auth_controller(flask_app)
