from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from app import db
from ...models.category import Category

categories_route = Blueprint('categories', __name__)


@categories_route.route('/categorias')
@login_required
def home():
    try:
        categories = Category.query.filter_by(user_id=current_user.id).all()
    except: 
        pass
    return render_template('categories/home.html', categories=categories)

@categories_route.route('/nova-categoria', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        try:
            new_cat = Category()
            new_cat.name = request.form.get('name')
            new_cat.user_id = current_user.id

            db.session.add(new_cat)
            db.session.commit()

            flash('Categoria criada com sucesso!')

        except SQLAlchemyError as error:
            flash(f'Ocorreu um erro ao adicionar a categoria "{request.form.get('name')}" erro: {error}')
            
        finally:
            db.session.close()

        return redirect(url_for('categories.new'))

    return render_template('categories/new.html')

@categories_route.route('/categorias/<id>/')
@login_required
def read(id):
    if not id:
        flash("Erro ao recuperar a categoria! (ID não recebido)")

    category = Category.query.filter_by(id=id).first()

    return render_template('categories/read.html', category=category)

@categories_route.route('/')
@login_required
def update(id):
    pass

@categories_route.route('/')
@login_required
def delete(id):
    pass
