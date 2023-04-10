from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Bloco import Bloco


class TelaLogin(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)

        self.rl = RelativeLayout() # Layout relativo, cujas estruturas requerem que uma localização seja inserida para os objetos inseridos

        bloco = Bloco(.5,.5,{'center_x': .4, 'center_y': .6})
        bloco.setFormat("retangulo_arredondado",(1,0,0,1))

        Button = PersonalButton(action=self.acao,size_hint=(.09, .05),
                        pos_hint={'center_x': .3, 'center_y': .5},
                        text="Teste",colorButton=(1,1,1,1),colorText=(0,0,0,1),textSize=15,format='retangulo_arredondado',borderColor=(1,0,1,1),borderSize=2)

        bloco.insertWidget(Button)

        self.rl.add_widget(bloco)
        self.add_widget(self.rl)
    

    def acao(self):
        pass
    

        
