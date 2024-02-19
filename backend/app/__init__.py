from flask import Flask
from app.extensions import configuration
from app.extensions import load_extensions


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    load_extensions.init_app(app)

    return app
