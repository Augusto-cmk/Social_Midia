from src.repository.person_status_repository import PersonStatusRepository
from src.schema.validation_schema import ValidationSchema
from src.schema.person_status_schema import PersonStatusSchema


class PersonStatusService(PersonStatusRepository):

    def __init__(self, data_person_status: dict) -> None:
        super().__init__()
        self._data_person_status = data_person_status
        self._validation_schema = PersonStatusSchema()

    def __init__(self):
        super().__init__()
    
    def create_status_person(self,person_id) -> dict:
        self._data_person_status = ValidationSchema.validation(self._data_person_status,
                                                               self._validation_schema)

        return self.insert_person_status(self._data_person_status,person_id)

    def get_person_status(self,id_person):
        return self.get_person_status(id_person)
