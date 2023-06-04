from marshmallow import Schema, fields, validate


class CommentSchema(Schema):
    text = fields.Str(
        required=True
    )

    date = fields.DateTime(
        required=True
    )

