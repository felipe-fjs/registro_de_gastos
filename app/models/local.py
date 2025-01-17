from app import db
from sqlalchemy import Column, Integer, String, ForeignKey

class Local(db.Model):
    __tablename__ = 'locals'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    