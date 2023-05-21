from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Visao.Telas.Login import TelaLogin
from Visao.Telas.Cadastro import TelaCadastro
from Visao.Telas.Chat import TelaChat
from Visao.Telas.Feed import TelaFeed
from Comunication.cliente import Cliente
from kivy.core.window import Window
import sys

class GerenciadorTelas(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.telas = {'login':TelaLogin,'cadastro':TelaCadastro,'chat':TelaChat,'feed':TelaFeed}
        self.cliente = Cliente()
        self.cliente.start()
        self.add_widget(TelaLogin(self))

    def go_to(self,nomeTela):
        return self.telas[nomeTela]

    def get_client(self):
        return self.cliente
    
    def close_cliet(self):
        self.cliente.stop_client()


class BrainCase(App):

    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        self.gerenciador = GerenciadorTelas()
        return self.gerenciador

    def on_request_close(self, *args):
        sys.exit(0)

BrainCase().run()