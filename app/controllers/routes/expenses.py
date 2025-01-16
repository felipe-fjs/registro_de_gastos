from app import db
from flask import Blueprint, request, render_template, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from ...models.expenses import Expenses
from ...models.local import Local   
from ...models.category import Category

expenses_route = Blueprint('expenses', __name__)

@expenses_route.route("/novo-gasto", methods=['GET', 'POST'])
# @login_required
def new_expense():
    if request.method == 'POST':
        try:
            # cria o novo gasto
            new_exp = Expenses()
            new_exp.title = request.form.get('title')
            new_exp.category_id = request.form.get('category_id')
            new_exp.amount = request.form.get('total')   
            new_exp.local_id = request.form.get('local_id')
            new_exp.date = request.form.get('data')

            # registra o novo gasto
            db.session.add(new_exp)
            db.session.commit()
        except SQLAlchemyError:
            flash(f"Ocorreu um erro ao registrar o gasto '{request.form.get('title')}'!")
    
        return redirect(url_for('expenses.new_expense'))
    
    # pegar informações de categorias e loais já cadastrados em bando de dados
    try:
        local = Local.query.all()
        category = Category.query.all()
    except SQLAlchemyError:
        flash("Ocorreu um erro ao carregar informações de categoria ou locais")

    return render_template("expenses/new.html", local=local, category=category)

