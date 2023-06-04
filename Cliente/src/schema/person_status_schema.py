from marshmallow import Schema, fields


class PersonStatusSchema(Schema):
    profession = fields.Str(
         required=True
    )
    university = fields.Str(
         required=True
    )
    course = fields.Str(
         required=True
    )
    web_site = fields.Str(
         required=True
    )
    linkedin = fields.Str(
         required=True
    )