from src.connection.connection import Connection
from src.models.friend import Friend


class FriendRepository:

    def __init__(self) -> None:
        self.__session = Connection().get_session()

    @staticmethod
    def create_friendship(person_id: int, friend_id: int) -> bool:
        friendship = Friend(person_id=person_id, friend_id=friend_id)
        friendship.save()

        return True