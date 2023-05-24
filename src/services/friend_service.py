from src.repository.friend_repository import FriendRepository


class FriendService(FriendRepository):
    def __init__(self):
        super().__init__()

    def create_friends(self, id_person: int, id_friend: int) -> None:
        self.create_friendship(id_person, id_friend)

    
