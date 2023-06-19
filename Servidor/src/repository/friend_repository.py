from src.connection.connection import Connection
import sqlite3


class FriendRepository:
    def __init__(self) -> None:
        self.__connection = Connection().get_connection()

    def create_friendship(self, person_id: int, friend_id: int) -> bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(
                "INSERT INTO friend (person_id, friend_id) VALUES (?, ?)",
                (person_id, friend_id)
            )
            self.__connection.commit()
            return True
        except sqlite3.Error:
            return False

    def delete_friendship(self, person_id: int, friend_id: int) -> bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(
                "DELETE FROM friend WHERE person_id = ? AND friend_id = ?",
                (person_id, friend_id)
            )
            self.__connection.commit()
            return True
        except sqlite3.Error:
            return False
