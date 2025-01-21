from app import db
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
import datetime
from .category import Category
from .local import Local

class Expenses(db.Model):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(150), nullable=False, default='Titulo não inserido')
    amount  = Column(Float, nullable=False, default=0.0)
    date = Column(DateTime(), nullable=False, default=datetime.datetime.now(datetime.UTC))
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    local_id = Column(Integer, ForeignKey('locals.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def get_category_name(self):
        if self.category_id:
            return Category.query.filter_by(id=self.category_id).first().name
        return f"Categoria não registrada ou não encontrada!"
        
    def get_local_name(self):
        if self.local_id:
            return Local.query.filter_by(id=self.local_id).first().name
        return f"Local não registrado ou não encontrado!"
        