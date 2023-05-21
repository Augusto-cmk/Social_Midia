import socket
from threading import Thread
from Comunication.mensagem import *
import queue
import sys
from src.services.person_service import PersonService
from src.services.person_status_service import PersonStatusService

class Server:
    def __init__(self) -> None:
        self.ip = socket.gethostbyname(socket.gethostname())
        self.porta = 8080
        self.address = (self.ip,self.porta)
        self.servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.servidor.bind(self.address)
        self.conexoes = {}
        self.server_client = Thread(target=self.__server_to_client)
        self.mensagens = queue.Queue()

    
    def start(self):
        print("[INFO] Servidor Iniciado")
        self.servidor.listen()
        self.server_client.start()
        while True:
            conn,addr = self.servidor.accept()
            thread = Thread(target=self.__clients_to_server,args=(conn,addr))
            thread.start()

    def __server_to_client(self):
        while True:
            retorno_servidor = None
            addr,msg = self.mensagens.get()
            # Realizar o tratamento da mensagem
            path = msg['route']
            if path == "cadastro":
                try:
                    person_service = PersonService(msg["person"])
                    id = person_service.register_person()
                    person_status_service = PersonStatusService(msg['status'])
                    person_status_service.create_status_person(id)
                    retorno_servidor = True
                except Exception:
                    retorno_servidor = False
            
            elif path == "login":
                email = msg['email']
                senha = msg['password']
                id = PersonService().login(email,senha)
                person = PersonService().get_person(id)
                status = PersonStatusService().get_person_status(id)
                print(person)
                print(status)

            #------------------------------
            # Depois, mandar a mensagem para o cliente
            msg_serialized = serialize(retorno_servidor)
            self.conexoes[addr].send(serialize({"size_buffer":sys.getsizeof(retorno_servidor)}))

            fragmentos = fragment_msg(msg_serialized,4096)
            for fragmento in fragmentos:
                self.conexoes[addr].send(fragmento)

    def __clients_to_server(self,conn,addr):
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
                            msg = deserialize(buffer) # Recebe a classe enviada pelo cliente (Obs: O servidor deve conhecer a estrutura da classe)
                            self.conexoes[addr] = conn
                            self.mensagens.put((addr,msg))
                            expected_size = sys.maxsize
                            buffer = b""
            
            except ConnectionResetError:
                print(f"[INFO] Cliente {addr} desconectou")
                break

servidor = Server()
servidor.start()