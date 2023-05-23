from src.repository.person_status_repository import PersonStatusRepository
from src.schema.validation_schema import ValidationSchema
from src.schema.person_status_schema import PersonStatusSchema


class PersonStatusService(PersonStatusRepository):

    def __init__(self) -> None:
        super().__init__()

    def create_status_person(self, person_id, data_person_status: dict) -> dict:
        _data_person_status = ValidationSchema.validation(data_person_status,
                                                          PersonStatusSchema())
        return self._insert_person_status(_data_person_status, person_id)

    def get_person_status(self, id_person):
        return self.get_status_person(id_person)
