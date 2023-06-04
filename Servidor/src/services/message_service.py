from src.repository.message_repository import MessageRepository


class MessageService(MessageRepository):

    def __init__(self):
        super().__init__()

    def send_message(self,self_id: int,id_destine: int,text: str) -> bool:
        return self._create_message(self_id,id_destine,text)
    
    def get_messages(self,id_author: int, id_destine: int) -> list:
        return self._get_messages(id_author,id_destine)