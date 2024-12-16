from app import db
from sqlalchemy import Column, Integer, String

class Category(db.Model):
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    