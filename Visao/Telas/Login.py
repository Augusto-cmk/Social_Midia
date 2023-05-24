from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Bloco import Bloco,BoxImage
from Visao.Recursos.checkbox import Interactive_Checkbox
from Visao.Recursos.Text import Text
from kivy.uix.label import Label
from Visao.Recursos.Popup import Alerta
from Controle.Envio_email import envioEmail
from Comunication.cliente import Cliente
from Modelo.user import User


class TelaLogin(Screen):
    def __init__(self,screenManager,**kw):
        super().__init__(**kw)
        self.screenManager = screenManager
        self.cliente:Cliente = self.screenManager.get_client()
        self.rl = RelativeLayout() # Layout relativo, cujas estruturas requerem que uma localização seja inserida para os objetos inseridos
        caixaLogin = Bloco(0.7,0.5,{'center_x':0.5,'center_y':0.5})
        caixaLogin.setFormat('retangulo_arredondado',(1,1,1,1))
        
        fundo = BoxImage('retangulo','Imagens/Fundo2.jpg',size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5})
        self.rl.add_widget(fundo)

        logo = BoxImage('retangulo','Imagens/Logo.png',size_hint=(.35,.3),pos_hint={'center_x':0.5,'center_y':0.75})

        btnLogin = PersonalButton(self.login,(1,1,1,1),(0,0,0,1),15,'retangulo_arredondado',pos_hint={'center_x':0.445,'center_y':0.25},size_hint=(0.09,0.05),text="Login",borderSize=1.5,borderColor=(0,0,0,1))
        btnCadastro = PersonalButton(self.cadastro,(1,1,1,1),(0,0,0,1),15,'retangulo_arredondado',pos_hint={'center_x':0.565,'center_y':0.25},size_hint=(0.09,0.05),text="Cadastro",borderSize=1.5,borderColor=(0,0,0,1))

        label_email = Label(text='E-mail',color='black',pos_hint={'center_x':0.35,'center_y':0.6},size_hint=(.09,.05))
        self.email = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),40,size_hint=(.37,.05),pos_hint={'center_x':0.5,'center_y':0.55})

        label_senha = Label(text='Senha',color='black',pos_hint={'center_x':0.35,'center_y':0.49},size_hint=(.09,.05))
        self.senha = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),40,size_hint=(.37,.05),pos_hint={'center_x':0.5,'center_y':0.44},password=True)

        btn_esqueci_senha = ImageButton(self.esqueci_senha,"Imagens/ForgotSenha.png",'retangulo',pos_hint={'center_x':0.5,'center_y':0.34},size_hint=(.25,.15))


        check_box = Interactive_Checkbox(self.exibirSenha,"Imagens/OlhoFechado.png",'Imagens/olhoAberto.png',pos_hint={'center_x':0.714,'center_y':0.44},size_hint=(.03,.025))

        caixaLogin.insertWidget(check_box)
        caixaLogin.insertWidget(btn_esqueci_senha)
        caixaLogin.insertWidget(label_senha)
        caixaLogin.insertWidget(self.senha)
        caixaLogin.insertWidget(label_email)
        caixaLogin.insertWidget(self.email)
        caixaLogin.insertWidget(btnLogin)
        caixaLogin.insertWidget(btnCadastro)
        caixaLogin.insertWidget(logo)

        self.rl.add_widget(caixaLogin)
        self.add_widget(self.rl)

    def exibirSenha(self,status):
        self.senha.password = not status

    def login(self):
        login = {
            "email":self.email.get_text(),
            "password":self.senha.get_text(),
            "route":"login"
        }
        self.cliente.input_mensage(login)
        resposta = self.cliente.get_msg_server()


        if resposta:
            person = resposta['person']
            status = resposta['status']
            colaborando = resposta['colaborando']
            colaboradores = resposta['colaboradores']
            user = User()
            user.set_nome(person['name'])
            user.set_colaborando(colaborando)
            user.set_colaboradores(colaboradores)
            user.set_id(person['id'])
            user.set_image_perfil(person['photo'])
            user.set_profissao(status['profession'])
            user.set_cidade(person['city'])
            user.set_estado(person['state'])
            user.set_curso(status['course'])
            user.set_data_nascimento(person['birthday'])
            user.set_email(person['email'])
            user.set_universidade(status['university'])
            user.set_web_site(status['web_site'])
            user.set_senha(person['password'])
            user.set_linkedin(status['linkedin'])
            self.clear_widgets()
            self.add_widget(self.screenManager.go_to('feed')(self.screenManager,user))
        else:
            alerta = Alerta()
            alerta.start("Erro","Não foi possível efetuar login, verifique seu email e senha!")
            self.rl.add_widget(alerta)

    def esqueci_senha(self):
        email = self.email.get_text()
        self.cliente.input_mensage({"route":"password","email":email})
        senha = self.cliente.get_msg_server()
        if senha:
            send = envioEmail(email,"Recuperação de senha",senha,"senha")
            if send:
                alerta = Alerta()
                alerta.start("Recuperação de senha",f"A senha foi enviada para {email}")
                self.rl.add_widget(alerta)
            else:
                alerta = Alerta()
                alerta.start("Erro","Algo deu errado ao tentar recuperar a senha, favor tentar novamente mais tarde!")
                self.rl.add_widget(alerta)
        else:
            alerta = Alerta()
            alerta.start("Erro","Você não possui cadastro no nosso sistema!")
            self.rl.add_widget(alerta)
    
    def cadastro(self):
        self.clear_widgets()
        self.add_widget(self.screenManager.go_to('cadastro')(self.screenManager))

        
