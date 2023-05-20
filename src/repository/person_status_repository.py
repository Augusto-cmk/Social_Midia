from src.connection.connection import Connection
from src.models.person_status import PersonStatus


class PersonStatusRepository:
    def __init__(self) -> None:
        self.__session = Connection().get_session()

    @staticmethod
    def insert_person_status(data_person_status: dict) -> None:
        person_status = PersonStatus(status_text=data_person_status.get("status_text"),
                                     profession=data_person_status.get("profession"),
                                     university=data_person_status.get("university"),
                                     course=data_person_status.get("course"),
                                     web_site=data_person_status.get("web_site"),
                                     linkedin=data_person_status.get("linkedin"))
        person_status.save()

    @staticmethod
    def update_person_status(self, person_status_id: str, updated_data: dict) -> None:
        try:
            person_status = PersonStatus.get(id=person_status_id)
        except Exception:
            raise Exception("PersonStatus não encontrado")

        person_status.status_text = updated_data.get("status_text", person_status.status_text)
        person_status.profession = updated_data.get("profession", person_status.profession)
        person_status.university = updated_data.get("university", person_status.university)
        person_status.course = updated_data.get("course", person_status.course)
        person_status.web_site = updated_data.get("web_site", person_status.web_site)
        person_status.linkedin = updated_data.get("linkedin", person_status.linkedin)

        person_status.save()

    def delete_person_status(self, id_person: int):
        try:
            self.__session.query(PersonStatus).filter(PersonStatus.person_id == id_person).delete()
            return {"mensagem": "Sucesso"}
        except Exception:
            return {"mensagem": "PersonStatus não encotrado"}