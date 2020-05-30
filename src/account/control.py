from flask import Blueprint

control = Blueprint('control', __name__)


@control.route('/panel')
def panel():
    return "control panel"