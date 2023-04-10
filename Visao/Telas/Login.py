from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Bloco import Bloco
from Visao.Recursos.Rolagem import caixaRolagem


class TelaLogin(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)

        self.rl = RelativeLayout() # Layout relativo, cujas estruturas requerem que uma localização seja inserida para os objetos inseridos

        self.add_widget(self.rl)

    

        
