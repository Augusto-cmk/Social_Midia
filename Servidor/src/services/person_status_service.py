import Pyro5.api
from src.repository.person_status_repository import PersonStatusRepository
from src.schema.validation_schema import ValidationSchema
from src.schema.person_status_schema import PersonStatusSchema

@Pyro5.api.expose
class PersonStatusService(PersonStatusRepository):

    def __init__(self) -> None:
        super().__init__()

    @Pyro5.api.expose
    def create_status_person(self, person_id, data_person_status: dict) -> dict:
        _data_person_status = ValidationSchema.validation(data_person_status,
                                                          PersonStatusSchema())
        return self._insert_person_status(_data_person_status, person_id)

    @Pyro5.api.expose
    def get_person_status(self, id_person):
        return self.get_status_person(id_person)

    @Pyro5.api.expose
    def refresh_status(self,person_id,updated_data: dict):
        return self._update_person_status(person_id,updated_data)
