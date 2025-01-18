from .expenses import expenses_route
from .categories import categories_route
from .account import account_route
from app import app

app.register_blueprint(expenses_route)
app.register_blueprint(categories_route)
app.register_blueprint(account_route)
