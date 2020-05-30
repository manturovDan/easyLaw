from flask import Blueprint, redirect, url_for, request
from src import db, create_app
from src.account import account_checker

lawyer = Blueprint('lawyer', __name__)

with create_app().app_context():
    engine = db.engine


@lawyer.before_request
def check_client_session():
    if not account_checker.check_session(engine):
        return redirect(url_for('auth.signout'))
    user = request.cookies.get('user')
    acc = account_checker.my_type(user, engine)
    if acc != 1:
        return redirect(url_for('account.center'))


@lawyer.route('/panel')
def panel():
    return "lawyer panel"


@lawyer.route('/consultation/<issue>')
def consultation(issue):
    return "consultation lawyer " + str(issue)


@lawyer.route('/new')
def new(issue):
    return "new issues"


@lawyer.route('/issue/<ticket>')
def bid(ticket):
    return "ticket " + str(ticket)