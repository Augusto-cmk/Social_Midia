import Pyro5.api
from src.repository.post_repository import PostRepository
from src.schema.validation_schema import ValidationSchema

@Pyro5.api.expose
class PostService(PostRepository):
    def __init__(self) -> None:
        super().__init__()

    @Pyro5.api.expose
    def create_post(self, data_post: dict) -> int:
        return self._create_post(data_post)

    @Pyro5.api.expose
    def get_posts(self, id_autor) -> list:
        return self.get_posts_user(id_autor)

    @Pyro5.api.expose
    def curtir_post(self, id_post) -> bool:
        try:
            self.add_like(id_post)
            return True
        except Exception:
            return False

    @Pyro5.api.expose
    def get_comments(self, post_id):
        return self.get_ordered_comments(post_id)
