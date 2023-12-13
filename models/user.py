import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

class UserModel(db.Model):

    __tablename__ = "User"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    passwd = db.Column(db.String(20), unique=False, nullable=False)
    shelf_id = db.Column(db.String(30), db.ForeignKey("Shelfs.shelf_id"), unique=False, nullable=False)
    shelf = db.relationship('Shelf', back_populates='user')