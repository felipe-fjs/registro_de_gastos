from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from app import db
from ...models.category import Category

categories_route = Blueprint('categories', __name__)

@categories_route.route('/nova-categoria', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        try:
            new_cat = Category()
            new_cat.name = request.form.get('name')

            db.session.add(new_cat)
            db.session.commit()

        except SQLAlchemyError:
            flash(f'Ocorreu um erro ao adicionar a categoria "{request.form.get('name')}"')
            
        finally:
            db.session.close()

        return redirect(url_for('categories.new_category'))

    return render_template('categories/new.html')
