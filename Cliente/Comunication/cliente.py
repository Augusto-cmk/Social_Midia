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
        self.person_service = Pyro5.api.Proxy(ns.lookup("person"))
        self.post_service = Pyro5.api.Proxy(ns.lookup("post_service"))
        self.comment_service = Pyro5.api.Proxy(ns.lookup("comment_service"))
        self.message_service = Pyro5.api.Proxy(ns.lookup("message_service"))
        self.friend_service = Pyro5.api.Proxy(ns.lookup("friend_service"))
        self.person_status_service = Pyro5.api.Proxy(ns.lookup("person_status_service"))

    def insert_comment(self, post_id, person_id, text):
        return self.comment_service.insert_comment(post_id, person_id, text)

    def create_friends(self, id_person, id_friend):
        return self.friend_service.create_friends(id_person, id_friend)

    def delete_friends(self, id_person, id_friend):
        return self.friend_service.delete_friends(id_person, id_friend)

    def send_message(self, self_id, id_destine, text):
        return self.message_service.send_message(self_id, id_destine, text)

    def get_messages(self, id_author, id_destine):
        return self.message_service.get_messages(id_author, id_destine)

    def create_status_person(self, person_id, data_person_status):
        return self.person_status_service.create_status_person(person_id, data_person_status)

    def get_person_status(self, id_person):
        return self.person_status_service.get_person_status(id_person)

    def refresh_status(self, person_id, updated_data):
        return self.person_status_service.refresh_status(person_id, updated_data)

    def get_comment(self, id_comment):
        return self.comment_service.get_comment(id_comment)

    def register_person(self, data_person):
        pass

    def refresh_perfil(self, id_person, data_person):
        pass

    def id_person(self, email, password):
        pass

    def get_password_person(self, email):
        pass

    def get_person(self, id):
        pass

    def get_friends_person(self, id_person):
        pass

    def get_post_friends_person(self, person_id):
        pass

    def get_len_colaborando(self, person_id):
        pass

    def get_len_colaboradores(self, person_id):
        pass

    def get_persons_all(self):
        pass


if __name__ == "__main__":
    cliente = Client()
    cliente.connect_to_server()
    print(cliente.get_person_status(1))
