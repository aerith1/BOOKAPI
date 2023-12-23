from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ShelfSchema, BorrowingSchema
from models import ShelfModel, BorrowingModel, LibraryModel
from get_uuid import generate_uuid
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

blp = Blueprint("Shelves", __name__, description="Operations on shelves")

@blp.route("/shelf/<int:user_id>")
@blp.response(200, ShelfSchema(many=True))
def get(user_id):
    return ShelfModel.query.filter_by(user_id=user_id).all()


@blp.route("/shelf/<int:user_id>/add_book")
class AddBookToShelf(MethodView):
    @blp.arguments(BorrowingSchema)
    @blp.response(200, ShelfSchema)
    def post(self, borrowing_data, user_id):
        shelf_book = ShelfModel.query.filter_by(book_id=borrowing_data['book_id'], user_id=user_id).first()
        book = LibraryModel.query.get(borrowing_data['book_id'])
        record = BorrowingModel.query.filter_by(borrowing_id=shelf_book.borrowing_id).first()

        if (not record.if_return):
            abort(401, message="Book alreay exits")
        if book:
            new_borrowing_id = generate_uuid()

            new_borrowing = BorrowingModel(
                borrowing_id=new_borrowing_id,
                borrowing_time=borrowing_data.get('borrowing_time'),
                returning_time=borrowing_data.get('returning_time'),
                user_id = user_id,
                if_return=borrowing_data.get('if_return', False),
            )
            LibraryModel.query.filter(LibraryModel.book_id == book.book_id).update({'amount_book': LibraryModel.amount_book-1})
            if(LibraryModel.query.get(borrowing_data['book_id']).amount_book < 0):
                abort(405, message="There is no book left")
            db.session.add(new_borrowing)
            db.session.commit()

            new_book = ShelfModel(
                shelf_id=generate_uuid(),
                book_id=borrowing_data['book_id'],
                user_id=user_id,
                borrowing_id=new_borrowing_id
            )

            db.session.add(new_book)
            db.session.commit()

            return new_book
        else:
            abort(404, message="Shelf or Book not found.")
