from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Bloco import Bloco,BoxImage
from Visao.Recursos.Rolagem import caixaRolagem
from Visao.Recursos.Text import Text


class TelaLogin(Screen):
    def __init__(self,screenManager,**kw):
        super().__init__(**kw)
        self.screenManager = screenManager
        self.rl = RelativeLayout() # Layout relativo, cujas estruturas requerem que uma localização seja inserida para os objetos inseridos
        caixaLogin = Bloco(0.9,0.5,{'center_x':0.5,'center_y':0.5})
        caixaLogin.setFormat('retangulo_arredondado',(1,1,1,1))
        
        fundo = BoxImage('retangulo','Imagens/Fundo2.jpg',size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5})

        logo = BoxImage('retangulo','Imagens/Logo.png',size_hint=(.35,.3),pos_hint={'center_x':0.5,'center_y':0.85})

        btnLogin = PersonalButton(self.login,(1,1,1,1),(0,0,0,1),15,'retangulo_arredondado',pos_hint={'center_x':0.445,'center_y':0.15},size_hint=(0.09,0.05),text="Login",borderSize=1.5,borderColor=(0,0,0,1))
        btnCadastro = PersonalButton(self.cadastro,(1,1,1,1),(0,0,0,1),15,'retangulo_arredondado',pos_hint={'center_x':0.565,'center_y':0.15},size_hint=(0.09,0.05),text="Cadastro",borderSize=1.5,borderColor=(0,0,0,1))

        self.rl.add_widget(fundo)
        caixaLogin.insertWidget(btnLogin)
        caixaLogin.insertWidget(btnCadastro)
        caixaLogin.insertWidget(logo)
        self.rl.add_widget(caixaLogin)
        self.add_widget(self.rl)

    def login(self):
        pass
    
    def cadastro(self):
        self.clear_widgets()
        self.add_widget(self.screenManager.go_to('cadastro')(self.screenManager))

        
