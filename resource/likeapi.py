from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import LikeSchema
from models import LikeModel, LibraryModel, BorrowingModel
from get_uuid import generate_uuid
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

blp = Blueprint("LikeList", __name__, description="Operations on LikeList")

@blp.route("/get_all_like/<int:user_id>")
@blp.response(200, LikeSchema(many=True))
def get_all_like(user_id):
    likes = LikeModel.query.filter_by(user_id=user_id).all()
    return likes

@blp.route("/add_like/<int:user_id>/<int:book_id>")
class AddLike(MethodView):
    @blp.response(200, LikeSchema)
    def post(self, user_id, book_id):
        like = LikeModel.query.filter_by(user_id=user_id, book_id=book_id).first()

        if not like:
            new_like = LikeModel(
                like_id=generate_uuid(),
                user_id=user_id,
                book_id=book_id,
            )

            db.session.add(new_like)
            db.session.commit()

            return new_like
        else:
            abort(400, message="Book already liked.")

@blp.route("/del_like/<int:user_id>/<int:book_id>")
class DelLike(MethodView):
    @blp.response(200, {"message": "Book unliked successfully."})
    def delete(self, user_id, book_id):
        like = LikeModel.query.filter_by(user_id=user_id, book_id=book_id).first()

        if like:
            db.session.delete(like)
            db.session.commit()
            return {"message": "Book unliked successfully."}
        else:
            abort(404, message="Book not found in liked list.")