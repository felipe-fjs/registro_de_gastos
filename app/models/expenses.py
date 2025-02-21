from app import db
from flask_login import current_user
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String, extract
from sqlalchemy.exc import SQLAlchemyError
import datetime
from .category import Category
from .local import Local

class Expenses(db.Model):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(40), nullable=False, default='Titulo não inserido')
    amount  = Column(Float, nullable=False, default=0.0)
    date = Column(DateTime(), nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    local_id = Column(Integer, ForeignKey('locals.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def get_category_name(self):
        if self.category_id:
            return Category.query.filter_by(id=self.category_id).first().name
        return f"Sem Categoria!"
        
    def get_local_name(self):
        if self.local_id:
            return Local.query.filter_by(id=self.local_id).first().name
        return f"Sem local!"

    def get_date(self):
        date = datetime.datetime.strftime(self.date, format="%d/%m/%Y %H:%M")
        return date

    def get_total_month():
        try:
            expenses = Expenses.query.filter_by(user_id=current_user.id).filter(
                extract('month', Expenses.date) == datetime.datetime.now(datetime.timezone.utc).month,
                extract('year', Expenses.date) == datetime.datetime.now(datetime.timezone.utc).year,
            ).all()

            sum = 0
            for expense in expenses:
                sum =sum + expense.amount
            return f'{sum:.2f}'
        except SQLAlchemyError:
            # registrar em log futuramente
            return 'erro'


