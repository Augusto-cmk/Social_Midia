from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Bloco import Bloco,BoxImage
from Visao.Recursos.Rolagem import caixaRolagem
from Visao.Recursos.Text import Text


class TelaLogin(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)
        self.rl = RelativeLayout() # Layout relativo, cujas estruturas requerem que uma localização seja inserida para os objetos inseridos
        txt = Text((1,1,1,1),(1,0,0,1),15,(0,0,0,1),pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.2,0.05),max_caracter=10,only_number=True)
        self.rl.add_widget(txt)
        self.add_widget(self.rl)

    def acao(self):
        pass    

        
