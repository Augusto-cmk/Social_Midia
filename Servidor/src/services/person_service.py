from src.repository.person_repository import PersonRepository
from src.schema.validation_schema import ValidationSchema
from src.schema.person_schema import PersonSchema
import Pyro5.api

@Pyro5.api.expose
class PersonService(PersonRepository):
    def __init__(self) -> None:
        super().__init__()
        self._validation_schema = PersonSchema()

    @Pyro5.api.expose
    def register_person(self, data_person):
        self._data_person = ValidationSchema.validation(data_person,
                                                        self._validation_schema)
        self.insert_person(data_person)

    @Pyro5.api.expose
    def refresh_perfil(self, id_person,data_person: dict):
        return self.refresh_profile(id_person,data_person)
    
    @Pyro5.api.expose
    def id_person(self, email: str, password: str) -> int:
        return self.get_person_id(email, password)
    
    @Pyro5.api.expose
    def get_password_person(self,email)->str:
        return self.get_person_password(email)
    
    @Pyro5.api.expose
    def get_person(self, id):
        return self.get_person_1(id)

    @Pyro5.api.expose
    def get_friends_person(self, id_person):
        return self.get_friends(id_person)

    @Pyro5.api.expose
    def get_post_friends_person(self, person_id):
        return self.get_person_posts(person_id)
    
    @Pyro5.api.expose
    def get_len_colaborando(self, person_id):
        return self.get_friends_count(person_id)

    @Pyro5.api.expose
    def get_len_colaborandores(self, person_id):
        return self.get_colaboradores_count(person_id)

    @Pyro5.api.expose
    def get_persons_all(self) -> list:
        return self.get_person_all()