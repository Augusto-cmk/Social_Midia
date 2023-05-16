from marshmallow import Schema, fields, validate



class PersonStatusSchema(Schema):
    status_text = fields.Str(
         required=True
    )
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