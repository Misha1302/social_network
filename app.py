from flask import Flask

app = Flask(__name__)

import controllers

if __name__ == 'main':
    app.run(debug=True)
