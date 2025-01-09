from app import db
from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError
from ...models.expenses import Expenses

expenses_route = Blueprint('expenses', __name__)

@expenses_route.route("/novo-gasto", methods=['GET', 'POST'])
# @login_required
def new_expense():
    if request.method == 'POST':
        try:
            new_exp = Expenses()
            new_exp.title = request.form.get('title')   
            new_exp.category = request.form.get('category')   
            new_exp.total = request.form.get('total')   
            new_exp.local = request.form.get('local')   
            new_exp.data = request.form.get('data')   
            with db.session as conn:
                conn.add(new_exp)
            return redirect(url_for('expenses.new_url'))
        except SQLAlchemyError:
            pass
        pass

    return render_template("expenses/new.html")

