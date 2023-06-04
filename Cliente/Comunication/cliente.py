import socket
from threading import Thread
from Comunication.mensagem import serialize, deserialize,fragment_msg
import queue
import sys

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
        self.is_running = False

    def input_mensage(self, mensagem):
        msg_serialized = serialize(mensagem)
        self.mensagem_to_send.put(serialize({"size_buffer":sys.getsizeof(msg_serialized)}))
        fragmentos = fragment_msg(msg_serialized,4096)
        for fragmento in fragmentos:
            self.mensagem_to_send.put(fragmento)

    def __client_to_server(self):
        while self.is_running:
            try:
                self.cliente.send(self.mensagem_to_send.get())
            except ConnectionResetError:
                print("[INFO] O Servidor desconectou-se")
                break

    def __server_to_client(self):
        buffer = b""
        expected_size = sys.maxsize
        while self.is_running:
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

            except ConnectionResetError:
                print("[INFO] O Servidor desconectou-se")
                break
    
    def get_msg_server(self):
        return self.mensagem_recived.get()

    def start(self):
        try:
            self.cliente.connect(self.addr)

        except ConnectionRefusedError:
            print("[INFO] O servidor está desconectado")
            return

        self.is_running = True
        self.thread_client_server.start()
        self.thread_client_to_server.start()

    def stop_client(self):
        self.is_running = False
        # Aguarda as threads serem encerradas
        self.thread_client_server.join()
        self.thread_client_to_server.join()
        self.cliente.close()