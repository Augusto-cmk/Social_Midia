from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Visao.Telas.Login import TelaLogin
from Visao.Telas.Cadastro import TelaCadastro

class GerenciadorTelas(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(TelaLogin())


class BrainCase(App):

    def build(self):
        return GerenciadorTelas()

BrainCase().run()