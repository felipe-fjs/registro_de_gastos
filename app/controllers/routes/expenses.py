from app import db
from flask import Blueprint, request, render_template, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from ...models.expenses import Expenses
import datetime

expenses_route = Blueprint('expenses', __name__)

@expenses_route.route("/novo-gasto", methods=['GET', 'POST'])
# @login_required
def new_expense():
    if request.method == 'POST':
        try:
            # cria o novo gasto
            new_exp = Expenses()
            new_exp.title = request.form.get('title')   
            new_exp.category_id = "1"
            new_exp.amount = request.form.get('total')   
            new_exp.local_id = "1"
            new_exp.date = request.form.get('data')
            print(new_exp.date)
            # registra o novo gasto
            db.session.add(new_exp)
            db.session.commit()
            print("FOI")
        except SQLAlchemyError:
            print("NÃO FOI")
            flash(f"Ocorreu um erro ao registrar o gasto '{request.form.get('title')}'")
    
        return redirect(url_for('expenses.new_expense'))

    data = datetime.datetime.now(datetime.UTC)
    print(data.isoformat())
    return render_template("expenses/new.html", data=data)

