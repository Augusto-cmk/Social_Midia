from src.repository.post_repository import PostRepository
from src.schema.validation_schema import ValidationSchema
from src.schema.post_schema import PostSchema


class PostService(PostRepository):
    def __init__(self) -> None:
        super().__init__()

    def create_post(self,data_post: dict):
        self._create_post(ValidationSchema.validation(data_post, PostSchema()))
