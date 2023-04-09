from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Botao import PersonalButton,ImageButton

class TelaLogin(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)

        self.rl = RelativeLayout() # Layout relativo, cujas estruturas requerem que uma localização seja inserida para os objetos inseridos

        Button = ImageButton(self.acao,"Imagens/mais.png","circulo",size_hint=(.09, .05),
                        pos_hint={'center_x': .5, 'center_y': .5})
                        
        self.rl.add_widget(Button)
        self.add_widget(self.rl)
    

    def acao(self):
        pass
    

        
