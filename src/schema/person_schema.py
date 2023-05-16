from marshmallow import Schema, fields, validate
from src.common.constants import age_min


class PersonSchema(Schema):
    name = fields.Str(
        required=True,
    )

    age = fields.Int(
        required=True,
        validate=[validate.Range(
            min=age_min
        )]
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
