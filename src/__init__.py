from flask import Flask
from src.auth.auth import auth


def create_app():

    app = Flask(__name__)
    app.register_blueprint(auth, url_prefix='/auth')

    return app