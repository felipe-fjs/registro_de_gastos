from app import db, bcrypt
from flask_login.mixins import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Float
import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    pwd = Column(String(64), unique=False, nullable=False)

    def verify_pwd(self, pwd):
        return bcrypt.check_password_hash(self.pwd, pwd)
    
    def new_pwd(self, pwd):
        self.pwd = bcrypt.generate_password_hash(pwd)


def current_time():
    return datetime.datetime.now(datetime.UTC)

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(160), nullable=False)
    birth = Column(Date(), nullable=False)
    created_at = Column(DateTime(), default=current_time(), nullable=False)
    updated_at = Column(DateTime(), default=current_time(), onupdate=current_time(), nullable=False)
    

class Balance(db.Model):
    __tablename__ = 'balances'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    total = Column(Float(precision=2), nullable=False, default=0.00)
    update_at = Column(DateTime(), default=current_time(), onupdate=current_time(), nullable=False)
