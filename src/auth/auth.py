from flask import Blueprint, render_template, request, redirect, url_for, make_response
from src.auth.auth_processing import AuthProcessing
from src import create_app
from src import db

auth = Blueprint('auth', __name__)

processing = None

with create_app().app_context():
    processing = AuthProcessing(db.engine)


@auth.route('/')
def login():
    return render_template('login.html')


@auth.route('/signin', methods=['POST'])
def signup_post():
    login = request.form.get('login')
    password = request.form.get('password')

    print(login + " " + password)
    hash = AuthProcessing.encrypt_string(password)
    print(hash)

    id, res = processing.auth_user(login, hash)
    if id == 0:
        return redirect(url_for('auth.login'))
    else:
        resp = make_response(render_template('setcookie.html'))
        resp.set_cookie('session', res)
        resp.set_cookie('user', str(id))
        return resp


@auth.route('/exit')
def signout():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    processing.out(user, session)

    resp = make_response(render_template('setcookie.html'))
    resp.delete_cookie('session')
    resp.delete_cookie('user')
    return resp