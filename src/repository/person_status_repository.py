from src.connection.connection import Connection
from src.models.person_status import PersonStatus
import sqlite3


class PersonStatusRepository:
    def __init__(self) -> None:
        self.__session = Connection().get_session()

    @staticmethod
    def _insert_person_status(data_person_status: dict, person_id: int) -> bool:
        try:
            person_status = PersonStatus(person_id=person_id,
                                         profession=data_person_status.get("profession"),
                                         university=data_person_status.get("university"),
                                         course=data_person_status.get("course"),
                                         web_site=data_person_status.get("web_site"),
                                         linkedin=data_person_status.get("linkedin"))
            person_status.save()
            return True
        except sqlite3.OperationalError as e:
            return False

    @staticmethod
    def _update_person_status(person_status_id: str, updated_data: dict) -> bool:
        try:
            person_status = PersonStatus.get(id=person_status_id)
        except Exception:
            raise Exception("PersonStatus não encontrado")

        person_status.profession = updated_data.get("profession", person_status.profession)
        person_status.university = updated_data.get("university", person_status.university)
        person_status.course = updated_data.get("course", person_status.course)
        person_status.web_site = updated_data.get("web_site", person_status.web_site)
        person_status.linkedin = updated_data.get("linkedin", person_status.linkedin)

        person_status.save()

    def get_status_person(self, person_id: int) -> bool:
        person_status = self.__session.query(PersonStatus).filter_by(person_id=person_id).first()

        if person_status is None:
            return False

        return person_status.__dict__

    def _delete_person_status(self, id_person: int) -> bool:
        try:
            self.__session.query(PersonStatus).filter(PersonStatus.person_id == id_person).delete()
            return True
        except Exception:
            return False
