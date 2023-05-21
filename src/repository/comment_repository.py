from src.connection.connection import Connection
from src.models.comment import Comment
import sqlite3
from datetime import datetime

class CommentRepository:

    def __init__(self) -> None:
        self.__session = Connection().get_session()

    @staticmethod
    def _create_comment(post_id: int, person_id: int, text: str) -> bool:
        try:
            comment = Comment(post_id=post_id, person_id=person_id, text=text, date=datetime.now())
            comment.save()
            return True
        except sqlite3.DataError:
            return False
        

    def _get_comment(self, id_comment: int) -> str:
        try:
            result = self.__session.query(Comment).get(id_comment)
            return result.__dict__
        except sqlite3.Error:
            return {}
