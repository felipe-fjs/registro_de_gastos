from app import db, login_manager, bcrypt
from flask_login.mixins import UserMixin
from sqlalchemy import Column, Integer, String

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    pwd = Column(String(64), unique=False, nullable=False)

    def verify_pwd(self, pwd):
        return bcrypt.check_password_hash(self.pwd, pwd)
    
    def new_pwd(self, pwd):
        self.pwd = bcrypt.generate_password_hash(pwd)
