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
        self.mensagem = Mensagem()
    
    def __client_to_server(self):
        while True:
            try:
                # input("Mandar classe: Press enter")
                # self.mensagem.set()
                # mensagem = self.mensagem.get()
                mensagem = input("Entre com uma mensagem: ")
                if mensagem:
                    self.cliente.send(serialize(mensagem))
            
            except ConnectionResetError:
                print("[INFO] O Servidor desconectou-se")
                break

    def __server_to_client(self):
        while True:
            try:
                msg = self.cliente.recv(4096)
                if msg:
                    msg = deserialize(msg) # Recebe a classe enviada pelo servidor (É necessário que o cliente conheça a estrutura da classe)
                    print("Mensagem recebida do servidor: ",msg)
            
            except ConnectionResetError:
                print("[INFO] O Servidor desconectou-se")
                break

    def start(self):
        try:
            self.cliente.connect(self.addr)

        except ConnectionRefusedError:
            print("[INFO] O servidor está desconectado")
            return

        self.thread_client_server.start()
        self.thread_client_to_server.start()

cliente = Cliente()
cliente.start()
