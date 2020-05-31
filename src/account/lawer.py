import json

from flask import Blueprint, redirect, url_for, request, render_template
from src import db, create_app
from src.account import account_checker, lawyer_processing, issue_processing, mesages_processing

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
    user = request.cookies.get('user')
    tickets = lawyer_processing.get_tickets(user, engine)
    return render_template('lawyer_panel.html', lawyer_name=account_checker.get_name(user, engine),
                           lawyer_status=lawyer_processing.get_lawyer_status(user, engine),
                           tick_len=len(tickets), my_tickets=tickets)


@lawyer.route('/consultation/<issue>')
def consultation(issue):
    user = request.cookies.get('user')
    if lawyer_processing.can_i_part(user, issue, engine):
        iss, lawyers = issue_processing.get_full_info(issue, engine)
        dialogues = issue_processing.get_dialogue(issue, engine)
        return render_template('lawyer_conv.html', id=issue, status = iss['status'], name = iss['name'], desc=iss['desc'], cr_date=iss['cr_time'], client_name=iss['client_name'], lawyers=lawyers, lawyers_count=len(lawyers),
                               dialogues=dialogues, client=0, messages = len(dialogues))
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


@lawyer.route('/ms_cnt/<issue>', methods=['GET'])
def ms_cnt(issue):
    if not issue_processing.allow_dialogue(request.cookies.get('user'), issue, engine):
        return "error", 101
    ret = len(issue_processing.get_dialogue(issue, engine))
    return str(ret)


@lawyer.route('/send/<issue>/<message>', methods=['GET'])
def send_msg(issue, message):
    if not issue_processing.allow_dialogue(request.cookies.get('user'), issue, engine):
        return "error", 101
    author = request.cookies.get('user')
    mesages_processing.send(issue, author, message, engine)
    return ""


@lawyer.route('/last/<issue>/<count>')
def last_msg(issue, count):
    if not issue_processing.allow_dialogue(request.cookies.get('user'), issue, engine):
        return "error", 101
    ret = issue_processing.get_dialogue(issue, engine, count)
    print(ret)
    for r in range(0, len(ret)):
        ret[r]['time'] = 0
    return json.dumps(ret)