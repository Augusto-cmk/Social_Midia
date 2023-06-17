import Pyro5.api
from src.repository.comment_repository import CommentRepository

@Pyro5.api.expose
class CommentService(CommentRepository):

    def __init__(self):
        super().__init__()

    @Pyro5.api.expose
    def insert_comment(self, post_id: int, person_id: int, text: str) -> bool:
        return self._create_comment(post_id, person_id, text)

    @Pyro5.api.expose
    def get_comment(self, id_comment: int) -> dict:
        return self._get_comment(id_comment)
