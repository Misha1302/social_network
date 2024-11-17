from flask import Flask

import controllers.controller


def init_controllers(flask_app: Flask):
    controllers.controller.init_controller(flask_app)
