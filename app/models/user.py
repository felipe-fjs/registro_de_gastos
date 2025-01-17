from app import db, login_manager
from flask_login.mixins import UserMixin
from sqlalchemy import Column, Integer, String

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    pwd = Column(String(128), unique=False, nullable=False)
