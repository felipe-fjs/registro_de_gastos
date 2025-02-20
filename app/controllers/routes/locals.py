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

