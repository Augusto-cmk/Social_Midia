from marshmallow import Schema, ValidationError

from src.repository.person_repository import PersonRepository


class PersonService(PersonRepository):
    def __init__(self, validation_schema: Schema):
        super().__init__()
        self._data_person = None
        self._validation_schema = validation_schema

    def validation_person(self, data_person: dict) -> dict:
        validate_data = {}
        is_valid = False
        while not is_valid:
            try:
                validate_data = self._validation_schema.load(data_person)
                self._data_person = validate_data
            except ValidationError as error:
                raise ValueError({"message": error.messages})

        return {"message": "success"}

    def register_person(self):
        self.insert_person(self._data_person)
