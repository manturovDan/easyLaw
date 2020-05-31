import json

from flask import Blueprint, redirect, url_for, request, render_template
from src import db, create_app
from src.account import account_checker, client_processing, issue_processing, mesages_processing

base = Blueprint('base', __name__)

with create_app().app_context():
    engine = db.engine


@base.route('/')
def base():
    blog = account_checker.get_blog(engine)
    print(blog)
    render_template('blog.html', blog=blog, count = len(blog))