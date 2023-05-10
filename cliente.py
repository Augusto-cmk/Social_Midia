import socket
from threading import Thread
from mensagem import *



class Cliente:
    def __init__(self) -> None:
        self.porta = 8080
        self.ip_servidor = "192.168.1.3"
        self.addr = (self.ip_servidor,self.porta)
        self.thread_client_server = Thread(target=self.__server_to_client)
        self.thread_client_to_server = Thread(target=self.__client_to_server)
        self.cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.cliente.connect(self.addr)
        self.mensagem = Mensagem()
    
    def __client_to_server(self):
        while True:
            # input("Mandar classe: Press enter")
            # self.mensagem.set()
            mensagem = self.mensagem.get()
            if mensagem:
                self.cliente.send(mensagem)

    def __server_to_client(self):
        while True:
            msg = self.cliente.recv(4096)
            if msg:
                msg = deserialize(msg) # Recebe a classe enviada pelo servidor (É necessário que o cliente conheça a estrutura da classe)

    def start(self):
        self.thread_client_server.start()
        self.thread_client_to_server.start()

cliente = Cliente()
cliente.start()
