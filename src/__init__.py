from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src import config

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = config.secret
    app.config['SQLALCHEMY_DATABASE_URI'] = config.db

    db.init_app(app)

    from src.auth.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from src.account.client import client
    app.register_blueprint(client, url_prefix='/client')

    from src.account.lawer import lawyer
    app.register_blueprint(lawyer, url_prefix='/lawyer')

    from src.account.control import control
    app.register_blueprint(control, url_prefix='/control')

    from src.account.account import account
    app.register_blueprint(account, url_prefix='/')


    return app