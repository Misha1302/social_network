from flask import *

app = Flask(__name__)

from requests import controllers

if __name__ == 'main':
    app.run(debug=True)

# so that the controllers import line is not considered unnecessary
controllers.useless()
