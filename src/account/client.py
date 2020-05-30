from flask import Blueprint, redirect, url_for, request
from src import db, create_app
from src.account import account_checker

client = Blueprint('client', __name__)

with create_app().app_context():
    engine = db.engine


@client.before_request
def check_client_session():
    if not account_checker.check_session(engine):
        return redirect(url_for('auth.signout'))
    user = request.cookies.get('user')
    acc = account_checker.my_type(user, engine)
    if acc != 0:
        return redirect(url_for('account.center'))


@client.route('/panel')
def panel():
    return "client panel"


@client.route('/consultation/<issue>')
def consultation(issue):
    return "consultation " + str(issue)