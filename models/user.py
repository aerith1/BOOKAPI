import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

class UserModel(db.Model):
    __tablename__ = "User"
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False)
    passwd = db.Column(db.String(20), unique=False, nullable=False)