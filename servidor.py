import socket
from threading import Thread
from mensagem import *

class Server:
    def __init__(self) -> None:
        self.ip = socket.gethostbyname(socket.gethostname())
        self.porta = 8080
        self.address = (self.ip,self.porta)
        self.servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.servidor.bind(self.address)
        self.buffer = []
        self.conexoes = {}
    
    def start(self):
        print("[INFO] Servidor Iniciado")
        self.servidor.listen()
        while True:
            conn,addr = self.servidor.accept()
            thread = Thread(target=self.__clients,args=(conn,addr))
            thread.start()
    
    def __clients(self,conn,addr):
        print(f"Um novo usuário se conectou pelo endereço = {addr}")
        while True:
            msg = conn.recv(4096)
            if msg:
                msg = deserialize(msg) # Recebe a classe enviada pelo cliente (Obs: O servidor deve conhecer a estrutura da classe)
                print(f"Mensagem recebida no servidor: {msg}")
                self.conexoes[addr] = conn

servidor = Server()
servidor.start()