from flask import Blueprint, redirect, url_for, request
from src import create_app
from src import db
from src.account import account_checker

account = Blueprint('account', __name__)

with create_app().app_context():
    engine = db.engine


@account.route('/')
def center():
    if not account_checker.check_session(engine):
        return redirect(url_for('auth.signout'))
    user = request.cookies.get('user')
    acc = account_checker.my_type(user, engine)
    if acc == 2:
        return redirect(url_for('control.panel'))
    elif acc == 1:
        return redirect(url_for('lawyer.panel'))
    else:
        return redirect(url_for('client.panel'))