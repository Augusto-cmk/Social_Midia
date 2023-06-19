from src.connection.connection import Connection
import sqlite3
from datetime import datetime


class MessageRepository:
    def __init__(self) -> None:
        self.__connection = Connection().get_connection()

    def create_message(self, author_id: int, destine_id: int, text: str) -> bool:
        try:
            cursor = self.__connection.cursor()
            date = datetime.now()
            cursor.execute(
                "INSERT INTO message (author_id, destine_id, text, date) VALUES (?, ?, ?, ?)",
                (author_id, destine_id, text, date)
            )
            self.__connection.commit()
            return True
        except sqlite3.Error:
            return False

    def obter_messages(self, id_author: int, id_destine: int) -> list:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(
                "SELECT * FROM message WHERE author_id = ? AND destine_id = ?",
                (id_author, id_destine)
            )
            results = cursor.fetchall()
            messages = []
            for result in results:
                message = {
                    "text": result[1],
                    "author_id": result[2],
                    "destine_id": result[3],
                    "date": result[4]
                }
                messages.append(message)
            return messages
        except sqlite3.Error:
            return []
