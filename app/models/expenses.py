from app import db
from sqlalchemy import Column, Integer, Float, DateTime
import datetime

class Expenses(db.Model):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, nullable=False)
    amount  = Column(Float, nullable=False, default=0.0)
    date = Column(DateTime(), nullable=False, default=datetime.datetime.now(datetime.UTC))
    category_id = Column(Integer, nullable=False)
    local_id = Column(Integer, nullable=False)
