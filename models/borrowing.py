import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

class BorrowingModel(db.Model):
    
    __tablename__='Borrowing'
    borrowing_id = db.Column(db.String(20), primary_key=True)
    borrowing_time = db.Column(db.DateTime)
    returning_time = db.Column(db.DateTime)
    if_return = db.Column(db.Boolean)