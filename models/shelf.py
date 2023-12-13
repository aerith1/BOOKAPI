import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

class ShelfModel(db.Model):

    __tablename__='Shelfs'
    shelf_id = db.Column(db.String(30), primary_key=True, unique=True)
    book_id = db.Column(db.Integer, db.ForeignKey('Library.book_id'), unique=True)
    # user_id = db.Column(db.Integer)
    borrowing_id = db.Column(db.String(20), db.ForeignKey('Borrowing.borrowing_id'))

    # user = db.relationship('User', back_populates='shelf')