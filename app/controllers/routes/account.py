from app import db, login_manager, bcrypt
from app.models.user import User
from flask import Blueprint,  render_template, request, redirect, url_for

account_route = Blueprint('account', __name__)

@login_manager.user_loader
def get_user(id):
    return User.query.filter_by(user_id=id).first()

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
