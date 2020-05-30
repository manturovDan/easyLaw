from flask import Blueprint, redirect, url_for, request, render_template
from src import db, create_app
from src.account import account_checker, lawyer_processing, issue_processing

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
    user = request.cookies.get('user')
    if lawyer_processing.can_i_part(user, issue, engine):
        iss, lawyers = issue_processing.get_full_info(issue, engine)
        return render_template('lawyer_conv.html', id=issue, status = iss['status'], name = iss['name'], desc=iss['desc'], cr_date=iss['cr_time'], lawyers=lawyers)
    return redirect(url_for('account.center'))


@lawyer.route('/new')
def new():
    tickets = lawyer_processing.get_free(engine)
    return render_template('lawyer_new_tickets.html', count=len(tickets), tickets=tickets)


@lawyer.route('/take/<issue>', methods=['POST'])
def take(issue):
    user = request.cookies.get('user')
    if lawyer_processing.take(user, issue, engine):
        return redirect(url_for('lawyer.consultation', issue=issue))
    else: #is taken
        return redirect(url_for('account.center')) #or err page