from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from CONFIG import SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/gerenciar_gastos'
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

# Registro dos modelos pelo arquivo models
import app.models.models as models

# Registro das rostas atraves do arquivo __init__ no diretorio routes
import app.controllers.routes as routes 
