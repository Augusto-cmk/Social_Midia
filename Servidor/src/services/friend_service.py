import Pyro5.api
from src.repository.friend_repository import FriendRepository

@Pyro5.api.expose
class FriendService(FriendRepository):
    def __init__(self):
        super().__init__()

    @Pyro5.api.expose
    def create_friends(self, id_person: int, id_friend: int) -> None:
        return self.create_friendship(id_person, id_friend)

    @Pyro5.api.expose
    def delete_friends(self,id_person: int, id_friend: int) -> bool:
        return self.delete_friendship(id_person,id_friend)

    
