from flask import Blueprint, render_template, request, redirect, url_for
from src.auth.auth_processing import AuthProcessing
from src import create_app
from src import db

auth = Blueprint('auth', __name__)

processing = None

with create_app().app_context():
    processing = AuthProcessing(db.engine)


@auth.route('/')
def go():
    return render_template('login.html')


@auth.route('/signin', methods=['POST'])
def signup_post():
    login = request.form.get('login')
    password = request.form.get('password')

    print(login + " " + password)
    hash = AuthProcessing.encrypt_string(password)
    print(hash)

    processing.auth_user(login, hash)

    return "lol"