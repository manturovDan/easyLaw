from flask import Blueprint, render_template, request, redirect, url_for
from src.auth.auth_processing import encrypt_string

auth = Blueprint('auth', __name__)

@auth.route('/')
def go():
    return render_template('login.html')


@auth.route('/signin', methods=['POST'])
def signup_post():
    login = request.form.get('login')
    password = request.form.get('password')

    print(login + " " + password)
    print(encrypt_string(password))


    return "lol"