import socket
from threading import Thread
from Comunication.mensagem import *
import queue
import sys
from src.services.person_service import PersonService
from src.services.person_status_service import PersonStatusService
from src.services.friend_service import FriendService
from src.services.post_service import PostService


class Server:
    def __init__(self) -> None:
        self.ip = socket.gethostbyname(socket.gethostname())
        self.porta = 8080
        self.address = (self.ip, self.porta)
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind(self.address)
        self.conexoes = {}
        self.server_client = Thread(target=self.__server_to_client)
        self.mensagens = queue.Queue()
        self.threads = {}

    def start(self):
        print("[INFO] Servidor Iniciado")
        self.servidor.listen()
        self.server_client.start()
        while True:
            conn, addr = self.servidor.accept()
            thread = Thread(target=self.__clients_to_server, args=(conn, addr))
            thread.start()
            self.threads[addr] = thread

    def __server_to_client(self):
        while True:
            retorno_servidor = None
            addr, msg = self.mensagens.get()
            # Realizar o tratamento da mensagem
            path = msg['route']
            if path == "cadastro":
                try:
                    person_service = PersonService()
                    person_service.register_person(msg["person"])
                    person_id = person_service.id_person(msg["person"]["email"], msg["person"]["password"])
                    person_status_service = PersonStatusService()
                    person_status_service.create_status_person(person_id, msg['status'])
                    retorno_servidor = True
                except Exception:
                    retorno_servidor = False

            elif path == "login":
                email = msg['email']
                senha = msg['password']
                try:
                    id = PersonService().id_person(email, senha)
                    person = PersonService().get_person(id)
                    status = PersonStatusService().get_person_status(id)
                    colaborando = PersonService().get_len_colaborando(id)
                    colaboradores = PersonService().get_colaboradores_count(id)
                    retorno_servidor = {'person': person, 'status': status,'colaborando':colaborando,'colaboradores':colaboradores}
                except Exception:
                    retorno_servidor = None
            
            elif path == "password":
                email = msg['email']
                password = PersonService().get_password_person(email)
                retorno_servidor = password

            elif path == "persons":
                persons = PersonService().get_persons_all()
                retorno_servidor = persons

            elif path == "friendship":
                try:
                    colaborando = PersonService().get_len_colaborando(msg['id'])
                    colaboradores = PersonService().get_colaboradores_count(msg['id'])
                except Exception:
                    colaboradores = 0
                    colaborando = 0

                retorno_servidor = {'colaborando':colaborando,'colaboradores':colaboradores}

            elif path == "status":
                status = PersonStatusService().get_person_status(msg['id'])
                retorno_servidor = status
            
            elif path == "colaborar":
                try:
                    FriendService().create_friends(msg['id_user'],msg['id_perfil'])
                    retorno_servidor = True
                except Exception:
                    retorno_servidor = False
            
            elif path == "friend_exist":
                try:
                    id = msg['id_user']
                    friends = PersonService().get_friends_person(id)
                    ids = [friend['id'] for friend in friends]
                    retorno_servidor = msg['id_perfil'] in ids
                except Exception:
                    retorno_servidor = False
            
            elif path == "post": # Ainda não funciona
                try:
                    PostService().create_post(msg['info_post'])
                    retorno_servidor = True
                except Exception:
                    retorno_servidor = False
            
            elif path == "posts":
                retorno_servidor = PostService().get_posts(msg['id'])
            
            elif path == 'friends':
                retorno_servidor = PersonService().get_friends_person(msg['id'])

            elif path == "close_friendship":
                retorno_servidor = FriendService().delete_friends(msg['id_user'],msg['id_perfil'])

            # ------------------------------
            # Depois, mandar a mensagem para o cliente
            msg_serialized = serialize(retorno_servidor)
            self.conexoes[addr].send(serialize({"size_buffer": sys.getsizeof(msg_serialized)}))

            fragmentos = fragment_msg(msg_serialized, 4096)
            for fragmento in fragmentos:
                self.conexoes[addr].send(fragmento)

    def __clients_to_server(self, conn, addr):
        print(f"Um novo usuário se conectou pelo endereço = {addr}")
        buffer = b""
        expected_size = sys.maxsize  # Inicialmente, não há um tamanho esperado
        while True:
            try:
                data = conn.recv(4096)
                if data:
                    if expected_size == sys.maxsize:
                        expected_size = deserialize(data)['size_buffer']
                    else:
                        buffer += data
                        if sys.getsizeof(buffer) >= expected_size:
                            msg = deserialize(
                                buffer)  # Recebe a classe enviada pelo cliente (Obs: O servidor deve conhecer a estrutura da classe)
                            self.conexoes[addr] = conn
                            self.mensagens.put((addr, msg))
                            expected_size = sys.maxsize
                            buffer = b""

            except ConnectionResetError:
                print(f"[INFO] Cliente {addr} desconectou")
                break


servidor = Server()
servidor.start()
