from flask import Blueprint, render_template, request, redirect, url_for, make_response
from src.auth.auth_processing import AuthProcessing
from src import create_app
from src import db
import src.account.account_checker

auth = Blueprint('auth', __name__)

processing = None

with create_app().app_context():
    processing = AuthProcessing(db.engine)


@auth.route('/')
def login():
    if src.account.account_checker.check_session(processing.engine):
        return redirect(url_for('auth.signout'))
    return render_template('login.html')


@auth.route('/signin', methods=['POST'])
def signup_post():
    if src.account.account_checker.check_session(processing.engine):
        return redirect(url_for('auth.signout'))
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

    resp = make_response(render_template('exit.html'))
    resp.delete_cookie('session')
    resp.delete_cookie('user')
    return resp