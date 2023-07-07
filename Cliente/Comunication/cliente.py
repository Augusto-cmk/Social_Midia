import Pyro5.api
from Interfaces.comment_service import CommentService
from Interfaces.friend_service import FriendService
from Interfaces.message_service import MessageService
from Interfaces.person_service import PersonService
from Interfaces.person_status_service import PersonStatusService
from Interfaces.post_service import PostService
from Interfaces.api_service import API

class Client:
    def __init__(self):
        self.person_service: PersonService = None
        self.post_service: PostService = None
        self.comment_service: CommentService = None
        self.message_service: MessageService = None
        self.friend_service: FriendService = None
        self.person_status_service: PersonStatusService = None
        self.api_service:API = None

    def connect_to_server(self):
        ns = Pyro5.api.locate_ns(host="localhost", port=9999)
        self.person_service = Pyro5.api.Proxy(ns.lookup("person_service"))
        self.post_service = Pyro5.api.Proxy(ns.lookup("post_service"))
        self.comment_service = Pyro5.api.Proxy(ns.lookup("comment_service"))
        self.message_service = Pyro5.api.Proxy(ns.lookup("message_service"))
        self.friend_service = Pyro5.api.Proxy(ns.lookup("friend_service"))
        self.person_status_service = Pyro5.api.Proxy(ns.lookup("person_status_service"))
        self.api_service = Pyro5.api.Proxy(ns.lookup("api"))