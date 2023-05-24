from src.connection.connection import Connection
from src.models.post import Post
from src.models.comment import Comment
import json


class PostRepository:
    def __init__(self) -> None:
        self.__session = Connection().get_session()

    def _create_post(self,data_post: dict) -> int:
        post = Post(text=data_post.get('text'),
                    image=data_post.get('image'),
                    curtir=data_post.get('curtir'),
                    date=data_post.get('date'),
                    author_id=data_post.get('author_id'))
        post.save()

    def add_like(self,id_post):
        post = self.__session.query(Post).filter(Post.id == id_post).order_by(Post.date).first()
        post.curtir += 1
        self.__session.commit()
        

    def get_posts_user(self,autor_id)->list:
        posts = self.__session.query(Post).filter(Post.author_id == autor_id).order_by(Post.date).all()
        posts_user = []
        for post in posts:
            data = {
                'id':post.id,
                'text':post.text,
                'image':post.image,
                'curtir':post.curtir,
                'date':post.date,
                'author_id':post.author_id
            }
            posts_user.append(data)
        return posts_user
    
    def get_posts_all(self):
        posts = self.__session.query(Post).all()
        for post in posts:
            print(post.text)

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
