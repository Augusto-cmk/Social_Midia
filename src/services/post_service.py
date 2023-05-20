from src.repository.post_repository import PostRepository
from src.schema.validation_schema import ValidationSchema
from src.schema.post_schema import PostSchema


class PostService(PostRepository):
    def __init__(self, data_post: dict) -> None:
        super().__init__()
        self._data_post = data_post
        self._validation_schema = PostSchema()

    def create_post(self):
        self._data_post = ValidationSchema.validation(self._data_post, self._validation_schema)
