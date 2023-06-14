import Pyro5.api as pyro
from src.services.person_service import PersonService
from src.services.post_service import PostService
from src.services.comment_service import CommentService
from src.services.message_service import MessageService
from src.services.friend_service import FriendService
from src.services.person_status_service import PersonStatusService

class ClientNameServer:
    def __init__(self) -> None:        
        # obtém a referência para o objeto remoto de person
        pyro.config.SERVERTYPE = "localhost"
        pyro.config.PORT = 5000
        pyro.config.HOST = "braincase"

        classes = ["person","post","comment","message","friend","person_status"]
        name_server = pyro.locate_ns()
        uris = [name_server.lookup(classe) for classe in classes]
        services_aux = [pyro.Proxy(uri) for uri in uris]
        self.services = {}
        for classe,service in zip(classes,services_aux):
            services_aux[classe] = service

    def get_person_service(self)->PersonService:
        return self.services['person']
    
    def get_post_service(self)->PostService:
        return self.services['post']
    
    def get_comment_service(self)->CommentService:
        return self.services['comment']

    def get_message_service(self)->MessageService:
        return self.services['message']

    def get_friend_service(self)->FriendService:
        return self.services['friend']

    def get_person_status_service(self)->PersonStatusService:
        return self.services['person_status']


cliente = ClientNameServer()