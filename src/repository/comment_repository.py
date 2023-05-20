from src.connection.connection import Connection
from src.models.comment import Comment


class CommentRepository:

    def __init__(self) -> None:
        self.__session = Connection().get_session()

    @staticmethod
    def create_comment(post_id: int, person_id: int, text: str) -> bool:
        comment = Comment(post_id=post_id, person_id=person_id, text=text)
        comment.save()

        return True

    def show_comment(self, id_comment: int) -> str:
        result = self.__session.query(Comment).get(id_comment)
        return result.text
