import socket
from threading import Thread
from mensagem import *
import queue
import sys

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
        self.size_buffer = 4096
    
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
            addr,msg = self.mensagens.get()
            # Realizar o tratamento da mensagem
            size_buffer = 6096*sys.getsizeof(serialize(msg))
            self.conexoes[addr].send(serialize({"size":size_buffer}))


            #------------------------------
            # Depois, mandar a mensagem para o cliente
            self.conexoes[addr].send(serialize(msg))

    def __clients_to_server(self,conn,addr):
        print(f"Um novo usuário se conectou pelo endereço = {addr}")
        while True:
            try:
                msg = conn.recv(self.size_buffer)
                if msg:
                    msg = deserialize(msg) # Recebe a classe enviada pelo cliente (Obs: O servidor deve conhecer a estrutura da classe)
                    try:
                        self.size_buffer = msg['size']
                        print("OPA")
                    except Exception:
                        print("Entrou no rolê")
                        self.size_buffer = 4096
                        foto = deserialize(msg['photo'])
                        self.conexoes[addr] = conn
                        self.mensagens.put((addr,msg))
            
            except ConnectionResetError:
                print(f"[INFO] Cliente {addr} desconectou")
                break

servidor = Server()
servidor.start()