from flask import Blueprint, redirect, url_for, request, render_template
from src import db, create_app
from src.account import account_checker, client_processing, issue_processing

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
    return render_template('client_panel.html', client_name = account_checker.get_name(user, engine), tick_len = len(tickets), my_tickets = tickets)


@client.route('/consultation/<issue>')
def consultation(issue):
    user = request.cookies.get('user')
    if not issue_processing.is_my_issue(user, issue, engine):
        return redirect(url_for('account.center'))
    iss, lawyers = issue_processing.get_full_info(issue, engine)
    dialogues = issue_processing.get_dialogue(issue, engine)
    return render_template('client_conv.html', id=issue, status=iss['status'], name=iss['name'], desc=iss['desc'],
                           cr_date=iss['cr_time'], client_name=iss['client_name'], lawyers=lawyers, lawyers_count=len(lawyers), dialogues=dialogues, client=1, messages = len(dialogues))


@client.route('/new')
def new():
    return render_template('new_ticket.html')


@client.route('/new_issue', methods=['POST'])
def new_issue():
    user = request.cookies.get('user')
    topic = request.form.get('subject')
    desc = request.form.get('desc')

    iss = issue_processing.new_ticket(user, topic, desc, engine)

    return redirect(url_for('client.consultation', issue = iss))


@client.route('/ticket_status/<issue>')
def get_status(issue):
    return issue_processing.get_status(issue, engine)


@client.route('/chat')
def chat():
    return render_template('chat.html')


@client.route('/ms_cnt/<issue>', methods=['GET'])
def ms_cnt(issue):
    ret = len(issue_processing.get_dialogue(issue, engine))
    print(ret)
    return str(ret)