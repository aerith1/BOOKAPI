from marshmallow import Schema, fields

class BookSchema(Schema):
    book_id = fields.Integer(dump_only=True)
    book_name = fields.Str(required=True, default="无职转生")
    author = fields.Str(required=True, default='satomi')
    introduction = fields.Str()
    amount_book = fields.Integer(required=True, default='0')
    average_score = fields.Decimal()
    cover_link = fields.Str(default='...')

class UpdateBookSchema(BookSchema):
    book_name = fields.Str()
    author = fields.Str()
    cover_link = fields.Str()


class BorrowingSchema(Schema):
    book_id = fields.Integer()
    borrowing_time = fields.DateTime()
    returning_time = fields.DateTime()

class ReturnSchema(Schema):
    user_id = fields.Integer()

class ShelfSchema(Schema):
    shelf_id = fields.Str(required=True)
    book_id = fields.Int(required=True)
    # user_id = fields.Str(required=True)
    borrowing_id = fields.Str()

class CheckRecordSchema(ShelfSchema):
    book_id = fields.Integer()
    if_return = fields.Boolean()
    borrowing_time = fields.DateTime()
    returning_time = fields.DateTime()

class UserSchema(Schema):
    user_id = fields.Str(dump_only=True)
    user_name = fields.Str()
    passwd = fields.Str(required=True)

class UserLoginSchema(Schema):
    user_name = fields.Str(required=True)
    passwd = fields.Str(required=True)



class LikeSchema(Schema):
    like_id = fields.Str(dump_only=True)
    book_id = fields.Int()
    user_id = fields.Int()

class ReviewSchema(Schema):
    review_id = fields.Str(dump_only=True)
    book_id = fields.Int()
    user_id = fields.Int()

class ReviewUpdateSchema(Schema):
    reviews = fields.Str()