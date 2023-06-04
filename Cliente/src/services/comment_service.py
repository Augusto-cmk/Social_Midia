from src.repository.comment_repository import CommentRepository


class CommentService(CommentRepository):

    def __init__(self):
        super().__init__()

    def insert_comment(self, post_id: int, person_id: int, text: str) -> bool:
        return self._create_comment(post_id, person_id, text)
    
    def get_comment(self, id_comment: int) -> dict:
        return self._get_comment(id_comment)
