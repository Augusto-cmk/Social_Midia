from src.repository.post_repository import PostRepository
from src.schema.validation_schema import ValidationSchema


class PostService(PostRepository):
    def __init__(self) -> None:
        super().__init__()

    def create_post(self,data_post: dict):
        self._create_post(data_post)
    
    def get_posts(self,id_autor)->list:
        return self.get_posts_user(id_autor)
