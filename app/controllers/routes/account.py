from app import db, login_manager, bcrypt
from flask import Blueprint,  render_template, request, redirect, url_for

account_route = Blueprint('account', __name__)

@account_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('account/login.html')


@account_route.route('/cadastro', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        pass

    return render_template('account/signup.html')
