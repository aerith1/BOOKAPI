import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
engine = create_engine('mysql+mysqlconnector://root:saber@localhost:3306/cit')
Base = declarative_base()

class BorrowingModel(Base):
    
    __tablename__='Borrowing'
    borrowing_id = Column(String(20), primary_key=True)
    borrowing_time = Column(DateTime, default=datetime.now)
    returning_time = Column(DateTime)
    user_id = Column(Integer)
    if_return = Column(Boolean, default=False)

class LibraryModel(Base):
    
    __tablename__='Library'
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(String(40), nullable=False)
    author = Column(String(30))
    introduction = Column(String(400))
    average_score = Column(Float(precision=2), unique=False)
    amount_book = Column(Integer)
    Cover_link = Column(String(200), nullable=True)

class UserModel(Base):

    __tablename__ = "User"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False)
    passwd = Column(String(20), unique=False, nullable=False)

class ShelfModel(Base):

    __tablename__='Shelfs'
    shelf_id = Column(String(30), primary_key=True)
    book_id = Column(Integer, ForeignKey('Library.book_id'))
    user_id = Column(Integer, ForeignKey('User.user_id'))
    borrowing_id = Column(String(20), ForeignKey('Borrowing.borrowing_id'))

class LikeModel(Base):
    __tablename__='LikeList'
    like_id = Column(String(30), primary_key=True)
    book_id = Column(Integer, ForeignKey('Library.book_id'))
    user_id = Column(Integer, ForeignKey('User.user_id'))

class ReviewsModel(Base):
    __tablename__='Reviews'
    review_id = Column(String(30), primary_key=True)
    book_id = Column(Integer, ForeignKey('Library.book_id'))
    user_id = Column(Integer, ForeignKey('User.user_id'))
    reviews = Column(String(200))
Base.metadata.create_all(engine)
