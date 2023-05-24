from src.connection.connection import Connection
from src.models.post import Post
from src.models.comment import Comment
from datetime import datetime
import json


class PostRepository:
    def __init__(self) -> None:
        self.__session = Connection().get_session()

    def _create_post(self,data_post: dict) -> None:
        post = Post(text=data_post.get('text'),
                    image=data_post.get('image'),
                    curtir=data_post.get('curtir'),
                    date=data_post.get('date'),
                    author_id=data_post.get('person_id'))
        post.save()

    def search_post_all(self) -> None:
        posts = self.__session.query(Post).all()
        for post in posts:
            # Tratar isso, se tiver foto ou não
            print(f'id:{post.id}, text:{post.text}, id_user:{post.author_id}')

    def get_post_comments(self, post_id: int):
        post = self.__session.query(Post).get(post_id)

        if post is None:
            return None

        comments = self.__session.query(Comment).filter(Comment.post_id == post_id).order_by(Comment.date).all()

        comments_data = []
        for comment in comments:
            comment_data = {
                'id': comment.id,
                'text': comment.text,
                'post_id': comment.post_id,
                'person_id': comment.person_id,
                'date': comment.date.strftime('%Y-%m-%d %H:%M:%S')
            }
            comments_data.append(comment_data)

        return json.dumps(comments_data)
