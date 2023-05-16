from src.connection.connection import Connection
from src.models.post import Post
from src.models.person import Person
from src.models.comment import Comment


class CommentRepository:

    def __init__(self) -> None:
        self.__session = Connection().get_session()

    def create_comment(self, post_id: int, person_id: int, text: str) -> bool:
        post = self.__session.query(Post).get(post_id)
        person = self.__session.query(Person).get(person_id)

        if post is None or person is None:
            return False

        comment = Comment(post=post, person=person, text=text)
        comment.save()

        return True
