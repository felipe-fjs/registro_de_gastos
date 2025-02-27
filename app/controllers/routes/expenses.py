from app import db
from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError
from ...models.expenses import Expenses
from ...models.local import Local   
from ...models.category import Category

expenses_route = Blueprint('expenses', __name__)


@expenses_route.route('/')
@expenses_route.route('/inicio')
@login_required
def home():
    expenses = Expenses.query.filter_by(user_id=current_user.id).all()
    month_sum = Expenses.get_total_month()
    return render_template('expenses/home.html', expenses=expenses, month_sum=month_sum)

@expenses_route.route("/novo-gasto", methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        try:
            # cria o novo gasto
            new_exp = Expenses()
            new_exp.title = request.form.get('title')
            new_exp.category_id = request.form.get('category_id')
            new_exp.amount = request.form.get('total')   
            new_exp.local_id = request.form.get('local_id')
            new_exp.date = request.form.get('data')
            new_exp.user_id = current_user.id

            # registra o novo gasto
            db.session.add(new_exp)
            db.session.commit()
        except SQLAlchemyError:
            flash(f"Ocorreu um erro ao registrar o gasto '{request.form.get('title')}'!")
    
        return redirect(url_for('expenses.new'))
    
    # pegar informações de categorias e loais já cadastrados em bando de dados
    try:
        local = Local.query.all()
        category = Category.query.all()
    except SQLAlchemyError:
        flash("Ocorreu um erro ao carregar informações de categoria ou locais")

    return render_template("expenses/new.html", local=local, category=category)


@expenses_route.route('/gasto-<id>/', methods=['GET'], defaults={'title': ''})
@expenses_route.route('/gasto-<id>/<title>', methods=['GET'])
@login_required
def read(id, title):
    if not id:
        flash('O ID do gasto não foi atribuido!')
        return redirect(url_for('expenses.home'))
    
    expense = Expenses.query.filter_by(id=id, user_id=current_user.id).first()
    return render_template('expenses/read.html', expense=expense)

@expenses_route.route('/gasto-<id>/edit', methods=['GET', 'PUT'], defaults={'title': ''})
@expenses_route.route('/gasto-<id>/<title>/edit', methods=['GET', 'PUT'])
@login_required
def update(id, title):
    if request.method == 'PUT':
        try:
            expense_updated = request.json
            expense_tobe_updated = Expenses.query.filter_by(id=expense_updated.id).first()

            expense_tobe_updated.title = expense_updated.title
            expense_tobe_updated.amount = expense_updated.amount
            expense_tobe_updated.date = expense_updated.date
            expense_tobe_updated.category_id = expense_updated.category_id
            expense_tobe_updated.local_id = expense_updated.local_id

            db.session.commit()
            flash(f"O gasto '{expense_updated.title[10]}...' foi atualizado!")
            return jsonify(success=True)
        except:
            flash("Ocorreu um erro ao atualizar o gasto!")
            return jsonify(success=False)

    if not id:
        flash('Gasto não localizado!')
        return redirect(url_for('expenses.home'))
    
    expense = Expenses.query.filter_by(id=id).first()
    return render_template('expenses/edit.html', expense=expense)


@expenses_route.route('/gasto-<id>/delete', methods=['GET', 'DELETE'], defaults={'title': ''})
@expenses_route.route('/gasto-<id>/<title>/delete', methods=['GET', 'DELETE'])
@login_required
def delete(id, title):
    if request.method == 'DELETE':
        try:
            expense = Expenses.query.filter_by(id=id).first()
            db.session.delete(expense)
            db.session.commit()
            
            flash('Gasto excluido com sucesso!')
            return jsonify(success=True)
            
        except: 
            flash('Erro ao excluir gasto!')
            return jsonify(success=False)
        
    if not id:
        return redirect(url_for('expenses.home'))
    
    try:
        expense = Expenses.query.filter_by(id=id).first()
    except :
        return redirect(url_for('expenses.read', id=id))
    
    return render_template('expenses/delete.html', expense=expense)