from src.connection.connection import Connection
from src.models.friend import Friend
import sqlite3


class FriendRepository:

    def __init__(self) -> None:
        self.__session = Connection().get_session()

    def create_friendship(self,person_id: int, friend_id: int) -> bool:
        try:
            friendship = Friend(person_id=person_id, friend_id=friend_id)
            friendship.save()
            return True
        except sqlite3.Error:
            return False
        