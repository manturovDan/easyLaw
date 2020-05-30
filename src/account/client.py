from flask import Blueprint

client = Blueprint('client', __name__)


@client.route('/panel')
def panel():
    return "client panel"


@client.route('/consultation/<issue>')
def consultation(issue):
    return "consultation " + str(issue)