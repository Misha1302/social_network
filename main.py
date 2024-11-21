from flask import *

from controllers import controllers_initializer

flask_app = Flask(__name__)

controllers_initializer.init_controllers(flask_app)

if __name__ == 'main':
    flask_app.run(debug=True)
