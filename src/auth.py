from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/auth')
def login():
    return 'login'