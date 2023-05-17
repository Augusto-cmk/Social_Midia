from src.connection.connection import Connection
from src.models.person_status import PersonStatus

class PersonStatusRepository:
    def __init__(self) -> None:
         self.__session = Connection().get_session()
    
    def insert_person_status(self,data_person_status:dict):
        person_status = PersonStatus(status_text=data_person_status.get("status_text"),
                            profession = data_person_status.get("profession"),
                            university = data_person_status.get("university"),
                            course = data_person_status.get("course"),
                            web_site = data_person_status.get("web_site"),
                            linkedin = data_person_status.get("linkedin"))
        person_status.save()
    
    def delete_person_status(self,id_person:int):
        self.__session.query(PersonStatus).filter(PersonStatus.person_id == id_person).delete()