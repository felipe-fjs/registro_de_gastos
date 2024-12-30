from flask import Blueprint, request, render_template

expenses_route = Blueprint('expenses', __name__)

@expenses_route.route("/novo-gasto", methods=['GET', 'POST'])
# @login_required
def new_expense():
    if request.method == 'POST':
        print(f'''
                titulo: {request.form.get('title')}
                total: {request.form.get('total')}
                categorie: {request.form.get('category')}
                local: {request.form.get('local')}
                data: {request.form.get('data')}
            ''')

    return render_template("expenses/new.html")

