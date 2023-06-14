import Pyro5.api as pyro
from src.services.person_service import *
from src.services.post_service import *
from src.services.comment_service import *
from src.services.message_service import *
from src.services.friend_service import *
from src.services.person_status_service import *

class NameServer:
    def __init__(self) -> None:
        pyro.config.SERVERTYPE = "braincase"
        pyro.config.HOST = "localhost"
        pyro.config.PORT = 5000
        # Inicia o name server
        pyro.start_ns()
        # criando instâncias para as services
        services = [PersonService(),PostService(),CommentService(),MessageService(),FriendService(),PersonStatusService()]
        # Configurando o objeto Pyro e registando os serviços no nameserver
        self.deamon = pyro.Daemon()
        uris = [self.deamon.register(service) for service in services]

        name_server = pyro.locate_ns()
        classes = ["person","post","comment","message","friend","person_status"]
        for classe,uri in zip(classes,uris):
            name_server.register(classe,uri)

    def start(self):
        self.deamon.requestLoop()

