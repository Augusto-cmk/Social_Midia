import socket
from threading import Thread
from mensagem import *
import queue
import cv2

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
            addr,msg = self.mensagens.get()
            # Realizar o tratamento da mensagem
            
            #------------------------------
            # Depois, mandar a mensagem para o cliente
            self.conexoes[addr].send(serialize(msg))

    def __clients_to_server(self,conn,addr):
        print(f"Um novo usuário se conectou pelo endereço = {addr}")
        while True:
            try:
                msg = conn.recv(100000)
                if msg:
                    msg = deserialize(msg) # Recebe a classe enviada pelo cliente (Obs: O servidor deve conhecer a estrutura da classe)
                    foto = deserialize(msg['photo'])
                    foto.resize((800,600))
                    cv2.imshow("teste",foto)
                    cv2.waitKey(0)
                    print(f"Mensagem recebida no servidor: {msg}")
                    self.conexoes[addr] = conn
                    self.mensagens.put((addr,msg))
            
            except ConnectionResetError:
                print(f"[INFO] Cliente {addr} desconectou")
                break

servidor = Server()
servidor.start()