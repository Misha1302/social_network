from flask import *

from controllers import controller_initializer

flask_app = Flask(__name__)

controller_initializer.init_controllers(flask_app)

if __name__ == 'main':
    flask_app.run(debug=True)
