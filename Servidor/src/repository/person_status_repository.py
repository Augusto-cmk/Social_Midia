from src.connection.connection import Connection
from src.models.person_status import PersonStatus
import sqlite3


class PersonStatusRepository:
    def __init__(self):
        self.__connection = Connection().get_connection()

    def _insert_person_status(self, data_person_status: dict, person_id: int) -> bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(
                "INSERT INTO person_status (person_id, profession, university, course, web_site, linkedin) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (
                    person_id,
                    data_person_status.get("profession"),
                    data_person_status.get("university"),
                    data_person_status.get("course"),
                    data_person_status.get("web_site"),
                    data_person_status.get("linkedin")
                )
            )
            self.__connection.commit()
            return True
        except sqlite3.OperationalError as e:
            return False

    def _update_person_status(self, person_id: str, updated_data: dict) -> bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(
                "UPDATE person_status SET course = ?, linkedin = ?, profession = ?, university = ?, web_site = ? "
                "WHERE person_id = ?",
                (
                    updated_data['course'],
                    updated_data['linkedin'],
                    updated_data['profession'],
                    updated_data['university'],
                    updated_data['web_site'],
                    person_id
                )
            )
            self.__connection.commit()
            return True
        except Exception:
            return False

    def get_status_person(self, person_id: int) -> bool:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM person_status WHERE person_id = ?", (person_id,))
        result = cursor.fetchone()
        if result is None:
            return False
        person_status = {
            'id': result[0],
            'person_id': result[1],
            'profession': result[2],
            'university': result[3],
            'course': result[4],
            'web_site': result[5],
            'linkedin': result[6]
        }
        return person_status

    def _delete_person_status(self, id_person: int) -> bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute("DELETE FROM person_status WHERE person_id = ?", (id_person,))
            self.__connection.commit()
            return True
        except Exception:
            return False
