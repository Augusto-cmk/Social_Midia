from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Visao.Telas.Login import TelaLogin
from Visao.Telas.Cadastro import TelaCadastro
from Visao.Telas.Chat import TelaChat
from Visao.Telas.Feed import TelaFeed
from Comunication.cliente import Cliente
from kivy.core.window import Window
import os
import signal

class GerenciadorTelas(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        caminho_pasta = 'temp'
        if not os.path.exists(caminho_pasta):
            os.mkdir(caminho_pasta)
        arquivos = os.listdir("temp")
        for arquivo in arquivos:
            os.remove(f"temp/{arquivo}")
        self.telas = {'login':TelaLogin,'cadastro':TelaCadastro,'chat':TelaChat,'feed':TelaFeed}
        self.cliente = Cliente()
        self.cliente.start()
        self.add_widget(TelaLogin(self))

    def go_to(self,nomeTela):
        return self.telas[nomeTela]

    def get_client(self):
        return self.cliente


class BrainCase(App):

    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        self.gerenciador = GerenciadorTelas()
        return self.gerenciador

    def on_request_close(self, *args):
        os.kill(os.getpid(),signal.SIGTERM)

BrainCase().run()