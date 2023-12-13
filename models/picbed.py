import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

class PicBedModel(db.Model):
    __tablename__='PicBed'
    png_id = db.Column(db.String(20), primary_key=True)
    book_id = db.Column(db.Integer)
    pgn_link = db.Column(db.String(200))