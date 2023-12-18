import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

class ReviewsModel(db.Model):
    __tablename__='Reviews'
    review_id = db.Column(db.String(30), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('Library.book_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    reviews = db.Column(db.String(200))