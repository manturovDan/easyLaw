from flask import Flask


def create_app():
    app = Flask(__name__)

    print(123)
    # blueprint for auth routes in our app
    from src.auth.auth import login as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='auth')

    # blueprint for non-auth parts of app
    #from .main import main as main_blueprint
    #app.register_blueprint(main_blueprint)

    return app