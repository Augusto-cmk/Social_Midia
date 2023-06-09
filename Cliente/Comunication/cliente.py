import socket
from threading import Thread
from Comunication.mensagem import serialize, deserialize,fragment_msg
import queue
import sys
import time

class Cliente:
    def __init__(self) -> None:
        self.porta = 8080
        self.ip_servidor = socket.gethostbyname(socket.gethostname())
        self.addr = (self.ip_servidor, self.porta)
        self.thread_client_server = Thread(target=self.__server_to_client)
        self.thread_client_to_server = Thread(target=self.__client_to_server)
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mensagem_to_send = queue.Queue()
        self.mensagem_recived = queue.Queue()
        self.resposta_servidor = queue.Queue()

    def input_mensage(self, mensagem):
        msg_serialized = serialize(mensagem)
        self.cliente.send(serialize({"size_buffer":sys.getsizeof(msg_serialized)}))
        fragmentos = fragment_msg(msg_serialized,4096)
        self.mensagem_to_send.put_nowait(fragmentos)

    def __client_to_server(self):
        while True:
            try:
                fragmentos = self.mensagem_to_send.get()
                for fragmento in fragmentos:
                    self.cliente.send(fragmento)
            except ConnectionRefusedError:
                print("[INFO] O Servidor desconectou-se")
                break

    def __server_to_client(self):
        buffer = b""
        expected_size = sys.maxsize
        while True:
            try:
                data = self.cliente.recv(4096)
                if data:
                    if expected_size == sys.maxsize:
                        expected_size = deserialize(data)['size_buffer']
                    else:
                        buffer += data
                        if sys.getsizeof(buffer) >= expected_size:
                            msg = deserialize(buffer)
                            self.mensagem_recived.put(msg)
                            expected_size = sys.maxsize
                            buffer = b""
                
                else:
                    print("[INFO] O Servidor desconectou-se")
                    break    

            except Exception:
                print("[INFO] O Servidor desconectou-se")
                break
    
    def get_msg_server(self):
        try:
            return self.mensagem_recived.get(timeout=20)
        except Exception:
            return None

    def start(self):
        try:
            self.cliente.connect(self.addr)

        except Exception:
            print("[INFO] O servidor está desconectado")
            return
        
        self.thread_client_server.start()
        self.thread_client_to_server.start()