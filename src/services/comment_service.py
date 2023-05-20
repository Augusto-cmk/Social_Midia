from marshmallow import Schema, ValidationError
from src.schema.validation_schema import ValidationSchema
from src.repository.comment_repository import CommentRepository
from src.schema.comment_schema import CommentSchema


class CommentService(CommentRepository):

    def __init__(self, data_comment: dict):
        super().__init__()
        self._data_comment = data_comment
        self._validation = CommentSchema()

    def insert_comment(self) -> None:
        self._data_comment = ValidationSchema.validation(self._data_comment,
                                                         self._validation)
