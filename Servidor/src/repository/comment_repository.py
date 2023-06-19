from src.connection.connection import Connection
import sqlite3
from datetime import datetime


class CommentRepository:
    def __init__(self):
        self.__connection = Connection().get_connection()

    def _create_comment(self, post_id: int, person_id: int, text: str) -> bool:
        try:
            cursor = self.__connection.cursor()
            date = datetime.now()
            cursor.execute(
                "INSERT INTO comment (post_id, person_id, text, date) VALUES (?, ?, ?, ?)",
                (post_id, person_id, text, date)
            )
            self.__connection.commit()
            return True
        except sqlite3.Error:
            return False

    def _get_comment(self, id_comment: int) -> dict:
        try:
            cursor = self.__connection.cursor()
            cursor.execute("SELECT * FROM comment WHERE id = ?", (id_comment,))
            result = cursor.fetchone()
            if result:
                comment = {
                    "id": result[0],
                    "post_id": result[1],
                    "person_id": result[2],
                    "text": result[3],
                    "date": result[4]
                }
                return comment
            return {}
        except sqlite3.Error:
            return {}
