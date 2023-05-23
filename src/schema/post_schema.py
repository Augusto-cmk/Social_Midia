from marshmallow import Schema, fields, validate


class PostSchema(Schema):
    text = fields.Str(
        required=True
    )

    image = fields.Str(
        required=True,
    )

    date = fields.DateTime(
        required=True
    )
