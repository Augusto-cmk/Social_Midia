import Pyro5.api
from src.repository.message_repository import MessageRepository

@Pyro5.api.expose
class MessageService(MessageRepository):

    def __init__(self):
        super().__init__()

    @Pyro5.api.expose
    def send_message(self,self_id: int,id_destine: int,text: str) -> bool:
        return self.create_message(self_id,id_destine,text)

    @Pyro5.api.expose
    def get_messages(self,id_author: int, id_destine: int) -> list:
        return self.obter_messages(id_author,id_destine)