from src.connection.connection import Connection
from src.models.message import Message
import sqlite3
from datetime import datetime


class MessageRepository:

    def __init__(self) -> None:
        self.__session = Connection().get_session()

    def _create_message(self,author_id: int, destine_id: int, text: str) -> bool:
        try:
            message = Message(author_id=author_id, destine_id=destine_id, text=text, date=datetime.now())
            message.save()
            return True
        except sqlite3.DataError:
            return False

    def _get_messages(self, id_author: int, id_destine: int) -> list:
        try:
            messages = self.__session.query(Message).filter(Message.author_id == id_author, Message.destine_id == id_destine).all()
            result = []
            for message in messages:
                value = {
                    "text":message.text,
                    "author_id":message.author_id,
                    "destine_id":message.destine_id,
                    "date":message.date
                }
                result.append(value)
            return result
        except sqlite3.Error:
            return {}
