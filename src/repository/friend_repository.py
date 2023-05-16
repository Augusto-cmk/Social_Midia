from src.connection.connection import Connection
from src.models.friend import Friend
from src.models.person import Person


class FriendRepository:

    def __init__(self) -> None:
        self.__session = Connection().get_session()

    def create_friendship(self, person_id: int, friend_id: int) -> bool:
        person = self.__session.query(Person).get(person_id)
        friend = self.__session.query(Person).get(friend_id)

        if person is None or friend is None:
            return False

        friendship = Friend(person=person, friend=friend)
        friendship.save()

        return True
