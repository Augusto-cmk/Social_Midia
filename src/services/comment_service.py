from src.schema.validation_schema import ValidationSchema
from src.repository.comment_repository import CommentRepository
from src.schema.comment_schema import CommentSchema


class CommentService(CommentRepository):

    def __init__(self, data_comment: dict):
        super().__init__()
        self._data_comment = data_comment
        self._validation = CommentSchema()

    def insert_comment(self, post_id: int, person_id: int, text: str) -> bool:
        self._data_comment = ValidationSchema.validation(self._data_comment,
                                                         self._validation)
        return self._create_comment(post_id, person_id, text)
    
    def get_comment(self, id_comment: int) -> dict:
        return self._get_comment(id_comment)
