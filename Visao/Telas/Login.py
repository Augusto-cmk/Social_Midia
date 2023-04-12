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
        caixaLogin = Bloco(0.5,0.5,{'center_x':0.5,'center_y':0.5})
        caixaLogin.setFormat('retangulo_arredondado',(1,1,1,1))

        btnLogin = PersonalButton(self.acao,(1,1,1,1),(0,0,0,1),15,'retangulo_arredondado',pos_hint={'center_x':0.445,'center_y':0.35},size_hint=(0.09,0.05),text="Login",borderSize=2,borderColor=(0,0,0,1))
        btnCadastro = PersonalButton(self.acao,(1,1,1,1),(0,0,0,1),15,'retangulo_arredondado',pos_hint={'center_x':0.565,'center_y':0.35},size_hint=(0.09,0.05),text="Cadastro",borderSize=2,borderColor=(0,0,0,1))

        caixaLogin.insertWidget(btnLogin)
        caixaLogin.insertWidget(btnCadastro)
        self.rl.add_widget(caixaLogin)
        self.add_widget(self.rl)

    def acao(self):
        pass    

        
