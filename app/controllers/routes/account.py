from app import db, login_manager
from app.models.user import User, Profile
from flask import Blueprint,  render_template, request, redirect, url_for, jsonify, flash
from flask_login import login_user, logout_user
from sqlalchemy.exc import SQLAlchemyError

account_route = Blueprint('account', __name__)

@login_manager.user_loader
def get_user(id):
    return User.query.filter_by(id=id).first()

@account_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            if not User.query.filter_by(email=request.form.get('email')).first():
                flash("Email não cadastrado!")
                return redirect(url_for('account.login'))
            
            user = User.query.filter_by(email=request.form.get('email')).first()
            if user.verify_pwd(request.form.get('pwd')):
                login_user(user)
                return redirect(url_for('expenses.home'))
            
            flash("Senha incorreta!")
            return redirect(url_for('account.login'))
        except SQLAlchemyError as error:
            pass

    return render_template('account/login.html')


@account_route.route('/cadastro', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # email já é verificado no formulário com um link a parte
        try:
            new_user = User()
            new_user.email = request.form.get('email')
            new_user.new_pwd(request.form.get('pwd'))

            db.session.add(new_user)
            db.session.flush()
            print(new_user.id)
            new_profile = Profile()
            new_profile.user_id = new_user.id
            new_profile.name = request.form.get('name')
            new_profile.birth = request.form.get('birth')
            print(new_profile.id)
            db.session.add(new_profile)

            db.session.commit()

        except SQLAlchemyError as error:
            flash(f'Ocorreu um erro ao tentar se registrar!{error}')
            return redirect(url_for('account.signup'))
        
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('account.login'))
    
    return render_template('account/signup.html')

@account_route.route('/verify-email/', defaults={'email':None})
@account_route.route('/verify-email/<email>')
def verify_email(email):
    if User.query.filter_by(email=email).first():
        return jsonify({'exists':True})
    
    return jsonify({'exists':False})
