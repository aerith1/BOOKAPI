import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import declarative_base
engine = create_engine('mysql+mysqlconnector://root:root@101.132.17.102:3306/cit')
Base = declarative_base()

class BorrowingModel(Base):
    
    __tablename__='Borrowing'
    borrowing_id = Column(String(20), primary_key=True)
    borrowing_time = Column(DateTime)
    returning_time = Column(DateTime)
    if_return = Column(Boolean)

class LibraryModel(Base):
    
    __tablename__='Library'
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(String(20), nullable=False)
    author = Column(String(20))
    introduction = Column(String(200))
    average_score = Column(Float(precision=2), unique=False)
    amount_book = Column(Integer)
    Cover_link = Column(String(200), nullable=True)
    

class ShelfModel(Base):

    __tablename__='Shelfs'
    shelf_id = Column(String(30), primary_key=True, unique=True)
    book_id = Column(Integer, ForeignKey('Library.book_id'), unique=True)
    # user_id = Column(Integer, ForeignKey(''))
    borrowing_id = Column(String(20), ForeignKey('Borrowing.borrowing_id'))

Base.metadata.create_all(engine)