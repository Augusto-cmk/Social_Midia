from src.repository.person_repository import PersonRepository
from src.schema.validation_schema import ValidationSchema
from src.schema.person_schema import PersonSchema


class PersonService(PersonRepository):
    def __init__(self) -> None:
        super().__init__()
        self._validation_schema = PersonSchema()

    def register_person(self, data_person):
        self._data_person = ValidationSchema.validation(data_person,
                                                        self._validation_schema)
        self.insert_person(self._data_person)

    def id_person(self, email: str, password: str) -> int:
        return self._get_person_id(email, password)
    
    def get_password_person(self,email)->str:
        return self._get_person_password(email)
    
    def get_person(self, id):
        return self._get_person(id)

    def get_friends_person(self, id_person):
        return self.get_friends(id_person)

    def get_post_friends_person(self, person_id):
        return self.get_person_posts(person_id)
    
    def get_len_colaborando(self, person_id):
        return self.get_friends_count(person_id)

    #def get_len_colaborandores(self, person_id):
    #    return self.get_friends_count(person_id)

    def get_persons_all(self) -> list:
        return self.get_person_all()
