import socket
from threading import Thread
from Comunication.mensagem import *
import queue
import sys
from src.services.person_service import PersonService
from src.services.person_status_service import PersonStatusService
from src.services.friend_service import FriendService
from src.services.post_service import PostService
from src.services.comment_service import CommentService
from src.services.message_service import MessageService
import time

class LogicalServer: # Serve para realizar a ação requisitada pelo usuário, ao acessar a posição ele realiza a operação
    def __init__(self) -> None:
        self.actions = {"cadastro":self.__cadastro,
                        "alterar dados usuário":self.__alterar_dados_usuario,
                        "login":self.__login,
                        "password":self.__password,
                        "persons":self.__persons,
                        "person":self.__person,
                        "friendship":self.__friendship,
                        "status":self.__status,
                        "colaborar":self.__colaborar,
                        "friend_exist":self.__friend_exist,
                        "post":self.__post,
                        "curtir":self.__curtir,
                        "posts":self.__posts,
                        "friends":self.__friends,
                        "close_friendship":self.__close_friendship,
                        "comment_post":self.__comment_post,
                        "comments_post":self.__comments_post,
                        "img_perfil":self.__img_perfil,
                        "send_msg":self.__send_msg,
                        "recive_msg":self.__recive_msg
                        }
    def get(self,key:str,msg:dict):
        return self.actions[key](msg)

    def __recive_msg(self,msg:dict):
        return MessageService().get_messages(msg['author'],msg['destine'])

    def __send_msg(self,msg:dict):
        return MessageService().send_message(msg['id_envio'],msg['id_recebe'],msg['text'])

    def __img_perfil(self,msg:dict):
        return PersonService().get_person(msg['id'])['photo']

    def __comments_post(self,msg:dict):
        return PostService().get_comments(msg['id_post'])

    def __comment_post(self,msg:dict):
        return CommentService().insert_comment(msg['post_id'],msg['person_id'],msg['text'])

    def __close_friendship(self,msg:dict):
        return FriendService().delete_friends(msg['id_user'],msg['id_perfil'])

    def __friends(self,msg:dict):
        return PersonService().get_friends_person(msg['id'])

    def __posts(self,msg:dict):
        return PostService().get_posts(msg['id'])
    
    def __curtir(self,msg:dict):
        return PostService().curtir_post(msg['id'])

    def __post(self,msg:dict):
        try:
            PostService().create_post(msg['info_post'])
            return True
        except Exception:
            return False

    def __friend_exist(self,msg:dict):
        try:
            id = msg['id_user']
            friends = PersonService().get_friends_person(id)
            ids = [friend['id'] for friend in friends]
            return msg['id_perfil'] in ids
        except Exception:
            return False

    def __colaborar(self,msg:dict):
        try:
            FriendService().create_friends(msg['id_user'],msg['id_perfil'])
            return True
        except Exception:
            return False

    def __status(self,msg:dict):
        status = PersonStatusService().get_person_status(msg['id'])
        return status
    
    def __friendship(self,msg:dict):
        try:
            colaborando = PersonService().get_len_colaborando(msg['id'])
            colaboradores = PersonService().get_colaboradores_count(msg['id'])
        except Exception:
            colaboradores = 0
            colaborando = 0

        return {'colaborando':colaborando,'colaboradores':colaboradores}

    def __person(self,msg:dict):
        return PersonService().get_person(msg['id'])
    
    def __persons(self,msg:dict):
        persons = PersonService().get_persons_all()
        return persons

    def __cadastro(self,msg:dict):
        try:
            person_service = PersonService()
            person_service.register_person(msg["person"])
            person_id = person_service.id_person(msg["person"]["email"], msg["person"]["password"])
            person_status_service = PersonStatusService()
            person_status_service.create_status_person(person_id, msg['status'])
            return True
        except Exception:
            return False
    
    def __password(self,msg:dict):
        email = msg['email']
        password = PersonService().get_password_person(email)
        return password

    def __login(self,msg:dict):
        email = msg['email']
        senha = msg['password']
        try:
            id = PersonService().id_person(email, senha)
            person = PersonService().get_person(id)
            status = PersonStatusService().get_person_status(id)
            colaborando = PersonService().get_len_colaborando(id)
            colaboradores = PersonService().get_colaboradores_count(id)
            return {'person': person, 'status': status,'colaborando':colaborando,'colaboradores':colaboradores}
        except Exception:
            return None

    def __alterar_dados_usuario(self,msg:dict):
        id = PersonService().id_person(msg["old"]["email"], msg["old"]["senha"])
        perfil_atualizado = PersonService().refresh_perfil(id,msg['person'])
        status_atualizado = PersonStatusService().refresh_status(id,msg['status'])
        return perfil_atualizado and status_atualizado

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
        self.ServerAction = LogicalServer()

    def start(self):
        print("[INFO] Servidor Iniciado")
        self.servidor.listen()
        self.server_client.start()
        while True:
            conn, addr = self.servidor.accept()
            thread = Thread(target=self.__clients_to_server, args=(conn, addr))
            thread.start()

    def __server_to_client(self):
        while True:
            retorno_servidor = None
            addr, msg = self.mensagens.get()
            # Realizar o tratamento da mensagem
            try:
                path = msg['route']
                retorno_servidor = self.ServerAction.get(path,msg)
                # ------------------------------
                # Depois, mandar a mensagem para o cliente
                msg_serialized = serialize(retorno_servidor)
                self.conexoes[addr].send(serialize({"size_buffer": sys.getsizeof(msg_serialized)}))

                fragmentos = fragment_msg(msg_serialized, 4096)
                time.sleep(0.1)
                for fragmento in fragmentos:
                    self.conexoes[addr].send(fragmento)
            except KeyError:
                print("[INFO] Erro de chave, mensagem mal interpretada no servidor")

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
                            msg = deserialize(buffer)  # Recebe a classe enviada pelo cliente (Obs: O servidor deve conhecer a estrutura da classe)
                            self.conexoes[addr] = conn
                            self.mensagens.put((addr, msg))
                            expected_size = sys.maxsize
                            buffer = b""
                
                else:
                    print(f"[INFO] Cliente {addr} desconectou")
                    break

            except Exception:
                print(f"[INFO] Cliente {addr} desconectou")
                break


Server().start()