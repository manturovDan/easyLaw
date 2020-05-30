from flask import Blueprint

lawyer = Blueprint('lawyer', __name__)


@lawyer.route('/panel')
def panel():
    return "lawyer panel"


@lawyer.route('/consultation/<issue>')
def consultation(issue):
    return "consultation lawyer " + str(issue)


@lawyer.route('/new')
def consultation(issue):
    return "new issues"


@lawyer.route('/issue/<ticket>')
def consultation(ticket):
    return "ticket " + str(ticket)