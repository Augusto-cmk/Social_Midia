from src.connection.connection import Connection
from src.models.person import Person
from src.models.post import Post
from src.models.friend import Friend
from src.models.comment import Comment

import json


class PersonRepository:
    def __init__(self):
        self.__session = Connection().get_session()

    def insert_person(self, data_person: dict) -> None:
        person = Person(name=data_person.get('name'),
                        age=data_person.get('age'),
                        photo=data_person.get('photo'),
                        email=data_person.get('email'),
                        password=data_person.get('password'),
                        state=data_person.get('state'),
                        city=data_person.get('city'),
                        birthday=data_person.get('birthday')
                        )
        person.save()

    def search_person_all(self) -> None:
        persons = self.__session.query(Person).all()
        for person in persons:
            print(f"ID: {person.id}, Nome: {person.name}, Idade: {person.age}")

    def get_person_id(self) -> int:
        result = self.__session.query(Person.id).filter(Person.name == "Jao").first()
        if result:
            person_id = result.id
            return person_id

    def get_friends_posts(self, person_id: int) -> str | None:
        person = self.__session.query(Person).get(person_id)

        if person is None:
            return None

        friends = self.__session.query(Friend).filter(Friend.person_id == person_id).all()
        friend_ids = [friend.friend_id for friend in friends]

        posts = self.__session.query(Post).filter(Post.author_id.in_(friend_ids)).order_by(Post.date.desc()).all()

        posts_data = []
        for post in posts:
            post_data = {
                'id': post.id,
                'text': post.text,
                'image': post.image,
                'likes': post.likes,
                'date': post.date.strftime('%Y-%m-%d %H:%M:%S'),
                'author_id': post.author_id
            }
            posts_data.append(post_data)

        return json.dumps(posts_data)

    def like_friend_post(self, person_id: int, post_id: int) -> bool:
        person = self.__session.query(Person).get(person_id)
        post = self.__session.query(Post).get(post_id)

        if person is None or post is None:
            return False

        post.likes += 1
        post.save()

        return True

    def comment_friend_post(self, person_id: int, post_id: int, text: str) -> bool:
        person = self.__session.query(Person).get(person_id)
        post = self.__session.query(Post).get(post_id)

        if person is None or post is None:
            return False

        comment = Comment(person=person, post=post, text=text)
        comment.save()

        return True