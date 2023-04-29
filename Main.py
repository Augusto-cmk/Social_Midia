from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Visao.Telas.Login import TelaLogin
from Visao.Telas.Cadastro import TelaCadastro
from Visao.Telas.Chat import TelaChat

class GerenciadorTelas(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.telas = {'login':TelaLogin,'cadastro':TelaCadastro,'chat':TelaChat}
        self.add_widget(TelaLogin(self))
    
    def go_to(self,nomeTela):
        return self.telas[nomeTela]


class BrainCase(App):

    def build(self):
        return GerenciadorTelas()

BrainCase().run()