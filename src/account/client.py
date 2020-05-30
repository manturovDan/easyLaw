from flask import Blueprint, redirect, url_for, request, render_template
from src import db, create_app
from src.account import account_checker, client_processing
import src.account.client_processing

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
    user = request.cookies.get('user')
    tickets = client_processing.get_tickets(user, engine)
    return render_template('client_panel.html', client_name = account_checker.get_login(user, engine), tick_len = len(tickets), my_tickets = tickets)


@client.route('/consultation/<issue>')
def consultation(issue):
    return "consultation " + str(issue)