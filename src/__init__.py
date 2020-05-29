from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dany:WWwin18Y@localhost:3306/law'

    db.init_app(app)

    from src.auth.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app