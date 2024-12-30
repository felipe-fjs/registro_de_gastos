from .expenses import expenses_route
from app import app

app.register_blueprint(expenses_route)
