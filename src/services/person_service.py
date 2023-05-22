

from src.repository.person_repository import PersonRepository
from src.schema.validation_schema import ValidationSchema
from src.schema.person_schema import PersonSchema

class PersonService(PersonRepository):
    def __init__(self) -> None:
        super().__init__()
        self._validation_schema = PersonSchema()

    def register_person(self,data_person):
        self._data_person = ValidationSchema.validation(data_person,
                                                        self._validation_schema)
        self.insert_person(self._data_person)

    def login(self, email: str, password: str) -> bool:
        return self._get_person_id(email, password)

    def get_person(self,id):
        return self._get_person(id)

