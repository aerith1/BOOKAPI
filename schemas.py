from marshmallow import Schema, fields

class BookSchema(Schema):
    book_id = fields.Int(dump_only=True)
    book_name = fields.Str(required=True)
    author = fields.Str(required=True)
    introduction = fields.Str()
    amount_book = fields.Integer(required=True)
    average_score = fields.Decimal()
    cover_link = fields.Str()

class UpdateBookSchema(BookSchema):
    book_name = fields.Str()
    author = fields.Str()
    cover_link = fields.Str()
