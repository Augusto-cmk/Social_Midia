from marshmallow import Schema, fields


class PersonSchema(Schema):
    name = fields.Str(
        required=True
    )

    birthday = fields.Str(
        required=True
    )

    photo = fields.Str(
        required=True
    )

    email = fields.Str(
        required=True
    )

    password = fields.Str(
        required=True
    )

    state = fields.Str(
        required=True
    )

    city = fields.Str(
        required=True
    )
