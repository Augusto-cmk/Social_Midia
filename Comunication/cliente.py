import socket
from threading import Thread
from Comunication.mensagem import serialize, deserialize
import queue

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
        self.mensagem_to_send.put(mensagem)

    def __client_to_server(self):
        while self.is_running:
            try:
                self.cliente.send(serialize(self.mensagem_to_send.get()))
            except ConnectionResetError:
                print("[INFO] O Servidor desconectou-se")
                break

    def __server_to_client(self):
        while self.is_running:
            try:
                msg = self.cliente.recv(100000)
                if msg:
                    msg = deserialize(msg)  # Recebe a classe enviada pelo servidor (É necessário que o cliente conheça a estrutura da classe)
                    # Recebe a mensagem do servidor e realiza a operacao desejada
                    self.mensagem_recived.put(msg)

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