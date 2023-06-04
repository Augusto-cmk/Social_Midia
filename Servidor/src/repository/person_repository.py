from src.connection.connection import Connection
from src.models.person import Person
from src.models.post import Post
from src.models.friend import Friend
from src.models.comment import Comment

import json


class PersonRepository:
    def __init__(self):
        self.__session = Connection().get_session()

    @staticmethod
    def insert_person(data_person: dict) -> None:
        person = Person(name=data_person.get('name'),
                        photo=data_person.get('photo'),
                        email=data_person.get('email'),
                        password=data_person.get('password'),
                        state=data_person.get('state'),
                        city=data_person.get('city'),
                        birthday=data_person.get('birthday')
                        )
        person.save()
    
    def refresh_profile(self,id_person,data_person: dict)->bool:
        try:
            person = self.__session.query(Person).filter(Person.id == id_person).first()
            person.birthday = data_person['birthday']
            person.city = data_person['city']
            person.email = data_person['email']
            person.name = data_person['name']
            person.password = data_person['password']
            person.photo = data_person['photo']
            person.state = data_person['state']
            self.__session.commit()
            return True
        except Exception:
            return False

    def get_person_all(self) -> list:
        persons = self.__session.query(Person).all()
        list_persons = []
        for person in persons:
            list_persons.append(person.__dict__)

        return list_persons

    def _get_person_password(self,email:str)->str:
        person = self.__session.query(Person).filter_by(email=email).first()
        if person is None:
            return None
        return person.password
    
    def _get_person_id(self, email: str, password: str) -> int:
        person = self.__session.query(Person).filter_by(email=email, password=password).first()

        if person is None:
            return None

        return person.id

    def _get_person(self, person_id):
        person = self.__session.query(Person).filter_by(id=person_id).first()
        try:
            return person.__dict__
        except Exception:
            return None

    def get_friends_posts(self, person_id: int) -> str:
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

    def get_friends(self, person_id: int):
        person = self.__session.query(Person).get(person_id)

        if person is None:
            return False

        friends = self.__session.query(Person).join(Friend, Friend.friend_id == Person.id).filter(
            Friend.person_id == person_id).all()

        person_friends = []
        for friend in friends:
            person_friends.append(friend.__dict__)

        return person_friends

    def get_person_posts(self, person_id: int) -> list:
        person = self.__session.query(Person).get(person_id)

        if person is None:
            return False

        posts = self.__session.query(Post).filter_by(author_id=person_id).all()
        list_posts = []
        for p in posts:
            list_posts.append(p.__dict__)
        return list_posts

    def get_friends_count(self, person_id: int) -> int:
        return len(self.get_friends(person_id))
    
    def get_colaboradores_count(self,person_id:int)->int:
        return len(self.__session.query(Friend).filter_by(friend_id=person_id).all())