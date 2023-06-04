from marshmallow import Schema, ValidationError


class ValidationSchema:

    @staticmethod
    def validation(data_person: dict, validation_schema: Schema) -> dict:
        validate_data = {}
        is_valid = False
        while not is_valid:
            try:
                validate_data = validation_schema.load(data_person)
                data_person = validate_data
                is_valid = True
            except ValidationError as error:
                raise ValueError({"message": error.messages})

        return data_person
