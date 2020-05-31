from flask import Blueprint, redirect, url_for, request, render_template
from src import create_app
from src import db
from src.account import account_checker, issue_processing

account = Blueprint('account', __name__)

with create_app().app_context():
    engine = db.engine


@account.route('/')
def center():
    if not account_checker.check_session(engine):
        return redirect(url_for('auth.signout'))
    user = request.cookies.get('user')
    acc = account_checker.my_type(user, engine)
    if acc == 2:
        return redirect(url_for('control.panel'))
    elif acc == 1:
        return redirect(url_for('lawyer.panel'))
    else:
        return redirect(url_for('client.panel'))


@account.route('/pay/<issue>')
def pay(issue):
    return render_template('pay.html', id = issue)


@account.route('/pay/<issue>', methods = ['POST'])
def pay_post(issue):
    issue_processing.pay(issue, engine)
    return redirect(url_for('account.center'))


@account.route('/base')
def blog():
    blog = account_checker.get_blog(engine)
    print(blog)
    return render_template('frequent.html', blog=blog, count = len(blog))


@account.route('/article/<art>')
def article(art):
    art = account_checker.get_art(art, engine)
    if art == None:
        return redirect('/')
    return render_template('article.html', topic=art['topic'], text=art['text'])
