from src.connection.connection import Connection
from src.models.post import Post
from datetime import datetime


class PostRepository:
    def __init__(self):
        self.__session = Connection().get_session()

    @staticmethod
    def create_post(data_post: dict) -> None:
        post = Post(text=data_post.get('text'),
                    image=data_post.get('image'),
                    curtir=0,
                    date=datetime.now(),
                    author_id=data_post.get('person_id'))
        post.save()

    def search_post_all(self) -> None:
        posts = self.__session.query(Post).all()
        for post in posts:
            print(f'id:{post.id}, text:{post.text}')