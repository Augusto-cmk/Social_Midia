from src.repository.person_repository import PersonRepository
from src.schema.validation_schema import ValidationSchema
from src.schema.person_schema import PersonSchema


class PersonService(PersonRepository):
    def __init__(self, data_person: dict) -> None:
        super().__init__()
        self._data_person = data_person
        self._validation_schema = PersonSchema()

    def register_person(self) -> None:
        self._data_person = ValidationSchema.validation(self._data_person,
                                                        self._validation_schema)
        print(self._data_person)
        self.insert_person()


if __name__ == '__main__':
    person_data1 = {
        'name': 'John Doe',
        'age': 21,
        'photo': 'john.jpg',
        'email': 'john@example.com',
        'password': 'password123',
        'state': 'California',
        'city': 'Los Angeles'
    }
    print(person_data1)
    print("ou")
    person = PersonService(person_data1)
    person.register_person()
