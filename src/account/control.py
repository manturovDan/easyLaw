from flask import Blueprint, redirect, url_for, request
from src import db, create_app
from src.account import account_checker

control = Blueprint('control', __name__)

with create_app().app_context():
    engine = db.engine


@control.before_request
def check_control_session():
    if not account_checker.check_session(engine):
        return redirect(url_for('auth.signout'))
    user = request.cookies.get('user')
    acc = account_checker.my_type(user, engine)
    if acc != 2:
        return redirect(url_for('account.center'))


@control.route('/panel')
def panel():
    return "control panel"