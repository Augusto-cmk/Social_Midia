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

        bloco = Bloco(.5,.5,{'center_x': .4, 'center_y': .6})
        bloco.setFormat("retangulo_arredondado",(1,0,0,1))

        button = PersonalButton(action=self.acao,size_hint=(.09, .05),
                        pos_hint={'center_x': .3, 'center_y': .5},
                        text="Teste",colorButton=(1,1,1,1),colorText=(0,0,0,1),textSize=15,format='retangulo_arredondado',borderColor=(1,0,1,1),borderSize=2)

        bloco.insertWidget(button)


        bloco2 = Bloco(.5,.5,{'center_x': .4, 'center_y': .6})
        bloco2.setFormat("retangulo_arredondado",(1,0,0,1))

        bloco2.insertWidget(PersonalButton(action=self.acao,size_hint=(.09, .05),
                        pos_hint={'center_x': .3, 'center_y': .5},
                        text="Teste",colorButton=(1,1,1,1),colorText=(0,0,0,1),textSize=15,format='retangulo_arredondado',borderColor=(1,0,1,1),borderSize=2))

        bloco3 = Bloco(.5,.5,{'center_x': .4, 'center_y': .6})
        bloco3.setFormat("retangulo_arredondado",(1,0,0,1))

        bloco3.insertWidget(PersonalButton(action=self.acao,size_hint=(.09, .05),
                        pos_hint={'center_x': .3, 'center_y': .5},
                        text="Teste",colorButton=(1,1,1,1),colorText=(0,0,0,1),textSize=15,format='retangulo_arredondado',borderColor=(1,0,1,1),borderSize=2))

        bloco3.insertWidget(Button(size_hint=(.12, .05),
                        pos_hint={'center_x': .5, 'center_y': .5},
                        text="Cadastrar"))

        rolagem = caixaRolagem([bloco,bloco2,bloco3])

        self.rl.add_widget(rolagem)
        self.add_widget(self.rl)
    

    def acao(self):
        pass
    

        
