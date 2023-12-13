from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import LibraryModel
from schemas import BookSchema, UpdateBookSchema
from sqlalchemy.exc import SQLAlchemyError
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

blp = Blueprint("books", __name__, description="Operations on books")

@blp.route("/book/<string:book_id>")
class Book(MethodView):
    @blp.response(200, BookSchema)
    def get(self, book_id):
        try:
            book = LibraryModel.query.filter_by(book_id=book_id).first()
            return book
        except KeyError:
            abort(404, message="book not found.")
    
    def delete(self, book_id):
        book = LibraryModel.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return {'message': 'Book deleted'}
    
    @blp.arguments(UpdateBookSchema)
    @blp.response(200, BookSchema)
    def put(self, book_data, book_id):
        book = LibraryModel.query.get(book_id)
        if book:
            book.name = book_data['book_name']
            book.author = book_data['author']
            book.introduction = book_data['introduction']
            book.amount_book = book_data['amount_book']
            book.cover_link = book_data['cover_link']
        else:
            book = LibraryModel(book_id=book_id, **book_data)
        
        db.session.add(book)
        db.session.commit()
        return book

    
    @blp.route("/book")
    class BookList(MethodView):
        @blp.response(200, BookSchema(many=True))
        def get(self):
            return LibraryModel.query.all()
        
        @blp.arguments(BookSchema)
        @blp.response(201, BookSchema)
        def post(self, book_data):
            book = LibraryModel(**book_data)
            try:
                db.session.add(book)
                db.session.commit()
            except SQLAlchemyError:
                abort(500, message="An error occurred while inserting the book.")

            return book_data