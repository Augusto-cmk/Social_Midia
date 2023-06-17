import Pyro5.api


class Client:
    def __init__(self):
        self.person_service = None
        self.post_service = None
        self.comment_service = None
        self.message_service = None
        self.friend_service = None
        self.person_status_service = None

    def connect_to_server(self):
        ns = Pyro5.api.locate_ns(host="localhost", port=9999)
        self.person_service = Pyro5.api.Proxy(ns.lookup("person_service"))
        self.post_service = Pyro5.api.Proxy(ns.lookup("post_service"))
        self.comment_service = Pyro5.api.Proxy(ns.lookup("comment_service"))
        self.message_service = Pyro5.api.Proxy(ns.lookup("message_service"))
        self.friend_service = Pyro5.api.Proxy(ns.lookup("friend_service"))
        self.person_status_service = Pyro5.api.Proxy(ns.lookup("person_status_service"))

    # Métodoso Post
    def create_post(self, data_post):
        return self.post_service.create_post(data_post)

    def get_posts(self, id_autor):
        return self.post_service.get_posts(id_autor)

    def curtir_post(self, id_post):
        return self.post_service.curtir_post(id_post)

    def get_comments(self, post_id):
        return self.post_service.get_comments(post_id)

    # Métodos para comment
    def insert_comment(self, post_id, person_id, text):
        return self.comment_service.insert_comment(post_id, person_id, text)

    def get_comment(self, id_comment):
        return self.comment_service.get_comment(id_comment)

    # Métodos para Menssage
    def send_message(self, self_id: int, id_destine: int, text: str) -> bool:
        return self.message_service.send_message(self_id, id_destine, text)

    def get_messages(self, id_author: int, id_destine: int) -> list:
        return self.message_service.get_messages(id_author, id_destine)

    # Métodos para friend
    def create_friends(self, id_person: int, id_friend: int) -> None:
        self.friend_service.create_friends(id_person, id_friend)

    def delete_friends(self, id_person: int, id_friend: int) -> bool:
        return self.friend_service.delete_friends(id_person, id_friend)

    # Métodos para person_status
    def create_status_person(self, person_id: int, data_person_status: dict) -> dict:
        return self.person_status_service.create_status_person(person_id, data_person_status)

    def get_person_status(self, id_person: int) -> dict:
        return self.person_status_service.get_person_status(id_person)

    def refresh_status(self, person_id: int, updated_data: dict):
        return self.person_status_service.refresh_status(person_id, updated_data)


if __name__ == "__main__":
    cliente = Client()
    cliente.connect_to_server()
    print(cliente.get_posts(1))
