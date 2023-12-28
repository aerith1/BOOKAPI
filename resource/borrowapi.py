from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ShelfSchema,CheckRecordSchema,BorrowingSchema,ReturnSchema
from models import ShelfModel, BorrowingModel, LibraryModel
from datetime import datetime
import pytz
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db
blp = Blueprint("Borrow", __name__, description="Check for borrowing record")

@blp.route("/<int:user_id>/borrowing")
@blp.response(200,CheckRecordSchema(many=True))
def get(user_id):
    records = db.session.query(ShelfModel.book_id, BorrowingModel.borrowing_id, BorrowingModel.if_return, BorrowingModel.borrowing_time, BorrowingModel.returning_time).join(BorrowingModel, ShelfModel.borrowing_id==BorrowingModel.borrowing_id).filter(ShelfModel.user_id==user_id).all()
    return records

@blp.route("/borrowing/<string:borrowing_id>", methods=["PUT"])
@blp.arguments(ReturnSchema)
@blp.response(200, CheckRecordSchema)
def return_book(data, borrowing_id):
    borrowing_record = BorrowingModel.query.filter(BorrowingModel.borrowing_id==borrowing_id).first()

    if not borrowing_record:
        abort(404, message="not found")
    borrowing_record.if_return = True

    chinatz = pytz.timezone("Asia/Shanghai")
    borrowing_record.returning_time = datetime.now(chinatz)


    db.session.commit()

    shelf_record = ShelfModel.query.filter_by(borrowing_id=borrowing_record.borrowing_id, user_id=data['user_id']).first()
    if shelf_record:
        library_record = LibraryModel.query.filter_by(book_id=shelf_record.book_id).first()
        if library_record:
            library_record.amount_book += 1
            db.session.commit()

    return borrowing_record
