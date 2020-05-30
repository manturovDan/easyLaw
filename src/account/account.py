from flask import Blueprint

account = Blueprint('account', __name__)


@account.route('/client_panel')
def client_panel():
    return "panel"


@account.route('/consultation/<issue>')
def consultation(issue):
    return "consultation control " + str(issue)