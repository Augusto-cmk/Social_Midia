import Pyro5.api
from Interfaces.comment_service import CommentService
from Interfaces.friend_service import FriendService
from Interfaces.message_service import MessageService
from Interfaces.person_service import PersonService
from Interfaces.person_status_service import PersonStatusService
from Interfaces.post_service import PostService


class Client:
    def __init__(self):
        self.person_service: PersonService = None
        self.post_service: PostService = None
        self.comment_service: CommentService = None
        self.message_service: MessageService = None
        self.friend_service: FriendService = None
        self.person_status_service: PersonStatusService = None

    def connect_to_server(self):
        ns = Pyro5.api.locate_ns(host="localhost", port=9999)
        self.person_service = Pyro5.api.Proxy(ns.lookup("person_service"))
        self.post_service = Pyro5.api.Proxy(ns.lookup("post_service"))
        self.comment_service = Pyro5.api.Proxy(ns.lookup("comment_service"))
        self.message_service = Pyro5.api.Proxy(ns.lookup("message_service"))
        self.friend_service = Pyro5.api.Proxy(ns.lookup("friend_service"))
        self.person_status_service = Pyro5.api.Proxy(ns.lookup("person_status_service"))


if __name__ == "__main__":
    client = Client()
    client.connect_to_server()
    print(client.comment_service.insert_comment(1,1,"oi"))
    print(client.comment_service.get_comment(1))
    print(client.message_service.get_messages(1,2))
    print(client.message_service.send_message(1,2,"oi"))

    '''
    print(client.person_service.get_person(1))
    print(client.person_service.get_friends_person(1))
    print(client.person_service.get_persons_all())
    print(client.person_service.get_len_colaborando(1))
    print(client.person_service.get_post_friends_person(1))
    '''