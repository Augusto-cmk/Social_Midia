import Pyro5.api
from src.services.person_service import PersonService
from src.services.post_service import PostService
from src.services.comment_service import CommentService
from src.services.message_service import MessageService
from src.services.friend_service import FriendService
from src.services.person_status_service import PersonStatusService
from threading import Thread
import os
import time
import platform


class Server:
    def __init__(self):
        Pyro5.config.SERVERTYPE = "multiplex"
        self.daemon = Pyro5.api.Daemon()

    def register_services(self):
        person_service = PersonService()
        post_service = PostService()
        comment_service = CommentService()
        message_service = MessageService()
        friend_service = FriendService()
        person_status_service = PersonStatusService()

        person_service_uri = self.daemon.register(person_service)
        post_service_uri = self.daemon.register(post_service)
        comment_service_uri = self.daemon.register(comment_service)
        message_service_uri = self.daemon.register(message_service)
        friend_service_uri = self.daemon.register(friend_service)
        person_status_service_uri = self.daemon.register(person_status_service)

        ns = Pyro5.api.locate_ns(host="localhost", port=9999)

        ns.register("person_service", person_service_uri)
        ns.register("post_service", post_service_uri)
        ns.register("comment_service", comment_service_uri)
        ns.register("message_service", message_service_uri)
        ns.register("friend_service", friend_service_uri)
        ns.register("person_status_service", person_status_service_uri)

    def start(self):
        print("Servidor pronto para aceitar conexões.")
        self.daemon.requestLoop()


def name_server():
    if platform.system() == "Linux":
        os.system("venv/bin/python3 -m Pyro5.nameserver --host=localhost --port=9999")
    else:
        os.system("python -m Pyro5.nameserver --host=localhost --port=9999")


def server():
    server = Server()
    server.register_services()
    server.start()


if __name__ == "__main__":
    nameserver = Thread(target=name_server)
    serv = Thread(target=server)
    nameserver.start()
    time.sleep(1)
    serv.start()
