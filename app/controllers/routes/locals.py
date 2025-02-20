from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from app import db
from ...models.local import Local

locals_route = Blueprint('locals', __name__)

@locals_route.route('/locais')
@login_required
def home():
    try:
        locals = Local.query.filter_by(user_id=current_user.id).all()
    except: 
        pass
    return render_template('locals/home.html', locals=locals)

@locals_route.route('/novo-local', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        try:
            new_local = Local()
            new_local.name = request.form.get('name')
            new_local.user_id = current_user.id

            db.session.add(new_local)
            db.session.commit()

            flash('Local registrado com sucesso!')

        except SQLAlchemyError as error:
            flash(f'Ocorreu um erro ao registrar o local "{request.form.get('name')}"')
            # registro de log para erros
            
        finally:
            db.session.close()

        return redirect(url_for('locals.new'))

    return render_template('locals/new.html')

@locals_route.route('/locais/<id>/')
@login_required
def read(id):
    if not id:
        flash("Erro ao recuperar a categoria! (ID não recebido)")

    local = Local.query.filter_by(id=id, user_id=current_user.id).first()
    # futuramente adicionar tabela com gastos que foram feito nesse local
    return render_template('locals/read.html', local=local)

