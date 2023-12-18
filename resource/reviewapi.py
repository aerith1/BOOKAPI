from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import LikeSchema, ReviewSchema, ReviewUpdateSchema
from models import ReviewsModel
from get_uuid import generate_uuid
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

blp = Blueprint("Reviews", __name__, description="I like reviewing")
@blp.route("/get_review/<int:book_id>")
@blp.response(200, ReviewSchema(many=True))
def get_all_like(book_id):
    likes = ReviewsModel.query.filter_by(book_id=book_id).all()
    return likes

@blp.route("/add_review/<int:user_id>/<int:book_id>")
class AddReview(MethodView):
    @blp.arguments(ReviewUpdateSchema)
    @blp.response(200, ReviewSchema)
    def post(self, reviewdata, user_id, book_id):
        new_review = ReviewsModel(
            review_id=generate_uuid(),
            user_id=user_id,
            book_id=book_id,
            reviews = reviewdata['reviews']
        )

        db.session.add(new_review)
        db.session.commit()

        return new_review

# @blp.route("/del_like/<int:user_id>/<int:book_id>")
# class DelLike(MethodView):
#     @blp.response(200, {"message": "Book unliked successfully."})
#     def delete(self, user_id, book_id):
#         like = LikeModel.query.filter_by(user_id=user_id, book_id=book_id).first()

#         if like:
#             db.session.delete(like)
#             db.session.commit()
#             return {"message": "Book unliked successfully."}
#         else:
#             abort(404, message="Book not found in liked list.")