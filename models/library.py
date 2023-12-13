import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

class LibraryModel(db.Model):
    __tablename__='Library'
    
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20))
    introduction = db.Column(db.String(200))
    average_score = db.Column(db.Float(precision=2), unique=False)
    amount_book = db.Column(db.Integer)
    cover_link = db.Column(db.String(200), nullable=True)
