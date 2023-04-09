from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Botao import PersonalButton

class TelaLogin(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)

        self.rl = RelativeLayout() # Layout relativo, cujas estruturas requerem que uma localização seja inserida para os objetos inseridos

        Button = PersonalButton(action=self.acao,size_hint=(.2, .05),
                        pos_hint={'center_x': .5, 'center_y': .5},
                        text="Teste",colorButton=(1,1,1,1),colorText=(0,0,0,1),textSize=15,format='retangulo_arredondado',borderColor=(1,0,1,1),borderSize=2)
                        
        self.rl.add_widget(Button)
        self.add_widget(self.rl)
    

    def acao(self):
        pass
    

        
