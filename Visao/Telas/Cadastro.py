from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Bloco import Bloco,BoxImage
from Visao.Recursos.Text import Text
from Visao.Recursos.Geometry import Geometry
from Visao.Recursos.checkbox import Interactive_Checkbox
from Controle.Envio_email import envioEmail,gerarNumero
from Visao.Recursos.Popup import Confirmar_Email,Alerta
from Visao.Recursos.choose_file import Choose_file
import cv2
from Comunication.mensagem import serialize
from Comunication.cliente import Cliente
import sys
from Controle.entrada import controleEntrada

class TelaCadastro(Screen):
    def __init__(self,screenManager,**kw):
        super().__init__(**kw)
        self.screenManager = screenManager
        self.cliente:Cliente = self.screenManager.get_client()

        self.rl = RelativeLayout() # Layout relativo, cujas estruturas requerem que uma localização seja inserida para os objetos inseridos
        
        fundo = BoxImage('retangulo','Imagens/Fundo2.jpg',size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5})

        # Bloco e imagem de perfil
        caixaCadastro = Bloco(0.96,0.9,{'center_x':0.5,'center_y':0.5})
        caixaCadastro.setFormat('retangulo_arredondado',(1,1,1,1))

        btnVoltar = ImageButton(self.voltar,"Imagens/Voltar.png","circulo",pos_hint={'center_x':0.1,'center_y':0.93},size_hint=(0.05,0.05))
        
        
        self.carregar_img = BoxImage("circulo",'Imagens/foto_perfil.jpg',pos_hint={'center_x':0.2,'center_y':0.81},size_hint=(0.2,0.2))
        btnImage_perfil = PersonalButton(self.foto_perfil,(1,1,1,1),(0,0,0,1),15,"retangulo_arredondado",pos_hint={'center_x':0.2,'center_y':0.66},size_hint=(0.15,0.05),borderSize=1.5,borderColor=(0,0,0,1),text='Inserir imagem')

        caixaCadastro.insertWidget(btnImage_perfil)
        caixaCadastro.insertWidget(btnVoltar)
        caixaCadastro.insertWidget(self.carregar_img)

        #___________________________________________________________________________________________


        # Nome
        asterisco_nome = Label(color='red',size_hint=(.2, .05),
                            pos_hint={'center_x': .415, 'center_y': .9}, text='*')

        label_nome = Label(color='black',size_hint=(.2, .05),
                            pos_hint={'center_x': .38, 'center_y': .9}, text='Nome')
        
        self.nome = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),28,pos_hint={'center_x':.5,'center_y':.85},size_hint=(.3,.05))
        
        caixaCadastro.insertWidget(label_nome)
        caixaCadastro.insertWidget(self.nome)
        caixaCadastro.insertWidget(asterisco_nome)
        #__________________________________


        # E-mail
        asterisco_email = Label(color='red',size_hint=(.2, .05),
                            pos_hint={'center_x': .415, 'center_y': .79}, text='*')
        label_email = Label(color='black',size_hint=(.2, .05),
                            pos_hint={'center_x': .38, 'center_y': .79}, text='E-mail')
        
        self.email = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),40,pos_hint={'center_x':.618,'center_y':.74},size_hint=(.54,.05))
        caixaCadastro.insertWidget(asterisco_email)
        caixaCadastro.insertWidget(label_email)
        caixaCadastro.insertWidget(self.email)
        #__________________________________

        #__________________________________
        
        # Input do aniversário

        asterisco_aniversario = Label(color='red',size_hint=(.2, .05),
                            pos_hint={'center_x': .855, 'center_y': .9}, text='*')
        
        label_aniversário = Label(color='black',size_hint=(.2, .05),
                            pos_hint={'center_x': .764, 'center_y': .9}, text='Data de nascimento')
        

        self.dia_aniversario = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),2,pos_hint={'center_x':.7,'center_y':.85},size_hint=(.04,.05),only_number=True)
        
        label_barra = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .735, 'center_y': .85}, text='/',font_size=25)
        
        self.mes_aniversario = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),2,pos_hint={'center_x':.77,'center_y':.85},size_hint=(.04,.05),only_number=True)

        label_barra2 = Label(color='black',size_hint=(.2, .05),
                            pos_hint={'center_x': .805, 'center_y': .85}, text='/',font_size=25)
        
        self.ano_aniversario = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),4,pos_hint={'center_x':.855,'center_y':.85},size_hint=(.07,.05),only_number=True)

        caixaCadastro.insertWidget(asterisco_aniversario)
        caixaCadastro.insertWidget(self.mes_aniversario)
        caixaCadastro.insertWidget(label_barra2)
        caixaCadastro.insertWidget(self.ano_aniversario)
        caixaCadastro.insertWidget(label_aniversário)
        caixaCadastro.insertWidget(self.dia_aniversario)
        caixaCadastro.insertWidget(label_barra)
        #__________________________________

        # Senha

        check_box = Interactive_Checkbox(self.exibirSenha,"Imagens/OlhoFechado.png",'Imagens/olhoAberto.png',pos_hint={'center_x':.746,'center_y':.63},size_hint=(.03,.025))
        asterisco_senha = Label(color='red',size_hint=(.2, .05),
                            pos_hint={'center_x': .412, 'center_y': .68}, text='*')

        label_senha = Label(text='Senha',color='black',pos_hint={'center_x':.377,'center_y':.68},size_hint=(.09,.05))
        self.senha = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,size_hint=(.37,.05),pos_hint={'center_x':.532,'center_y':.63},password=True)
        
        caixaCadastro.insertWidget(check_box)
        caixaCadastro.insertWidget(asterisco_senha)
        caixaCadastro.insertWidget(label_senha)
        caixaCadastro.insertWidget(self.senha)

        #___________________________________
        
        #________________________________________________________________________________________________________________

        separador = Geometry('retangulo',(0,0,0,0.2),pos_hint={'center_x':0.5,'center_y':0.57},size_hint=(.9,.003))

        caixaCadastro.insertWidget(separador)

        #________________________________________________________________________________________________________________


        label_estado = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .14, 'center_y': .52}, text='Estado')
        
        self.estado = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.23,'center_y':.47},size_hint=(.25,.05))
        caixaCadastro.insertWidget(label_estado)
        caixaCadastro.insertWidget(self.estado)

        #________________________________


        # Cidade

        label_cidade = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .41, 'center_y': .52}, text='Cidade')
        
        self.cidade = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.5,'center_y':.47},size_hint=(.25,.05))
        caixaCadastro.insertWidget(label_cidade)
        caixaCadastro.insertWidget(self.cidade)

        #________________________________


        # Profissão

        label_profissao = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .69, 'center_y': .52}, text='Profissão')
        
        self.profissao = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.77,'center_y':.47},size_hint=(.25,.05))
        caixaCadastro.insertWidget(label_profissao)
        caixaCadastro.insertWidget(self.profissao)

        #________________________________


        # Universidade

        label_universidade = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .165, 'center_y': .41}, text='Universidade')
        
        self.universidade = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.296,'center_y':.36},size_hint=(.385,.05))
        caixaCadastro.insertWidget(label_universidade)
        caixaCadastro.insertWidget(self.universidade)

        #________________________________


        # Curso

        label_curso = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .542, 'center_y': .41}, text='Curso')
        
        self.curso = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.704,'center_y':.36},size_hint=(.385,.05))
        caixaCadastro.insertWidget(label_curso)
        caixaCadastro.insertWidget(self.curso)

        #________________________________

        
        # Web Site

        label_website = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .148, 'center_y': .3}, text='Web Site')
        
        self.website = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),100,pos_hint={'center_x':.5,'center_y':.25},size_hint=(.795,.05))
        caixaCadastro.insertWidget(label_website)
        caixaCadastro.insertWidget(self.website)

        #________________________________


        # Linkedin

        label_linkedin = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .148, 'center_y': .19}, text='Linkedin')
        
        self.linkedin = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),100,pos_hint={'center_x':.5,'center_y':.14},size_hint=(.795,.05))
        caixaCadastro.insertWidget(label_linkedin)
        caixaCadastro.insertWidget(self.linkedin)

        #________________________________


        btnsalvar = PersonalButton(self.salvar,(1,1,1,1),(0,0,0,1),15,"retangulo_arredondado",pos_hint={'center_x':0.5,'center_y':0.057},size_hint=(0.15,0.05),borderSize=1.5,borderColor=(0,0,0,1),text='Salvar')
        caixaCadastro.insertWidget(btnsalvar)  

        self.rl.add_widget(fundo)
        self.rl.add_widget(caixaCadastro)
        self.add_widget(self.rl)
    
    def exibirSenha(self,status):
        self.senha.password = not status

    def foto_perfil(self):# Provavelmente vai ter que utilizar uma lógica de backend para inserir isso ao banco de dados e carregar dinamicamente na tela ao fazer upload da imagem
        self.dir_img = Choose_file().get_dir()
        self.carregar_img.set_new_img(self.dir_img)

    def salvar(self):
        # Código de confirmação de e-mail
        atributos_necessarios = [self.email.get_text(),self.senha.get_text(),self.nome.get_text(),self.dia_aniversario.get_text(),self.mes_aniversario.get_text(),self.ano_aniversario.get_text()]
        erros = ["O campo de email é obrigatorio","O campo de senha é obrigatorio","O campo do nome é obrigatorio","O campo dia do aniversário é obrigatorio","O campo mes do aniversário é obrigatorio","O campo ano do aniversário é obrigatorio"]
        for i,atributo in enumerate(atributos_necessarios):
            if atributo == '':
                alerta = Alerta()
                alerta.start("Erro",erros[i])
                self.rl.add_widget(alerta)

        codigo_email = gerarNumero()
        email = self.email.get_text()
        send = envioEmail(email,"Confirmação de e-mail",codigo_email,'confirmar')
        if send:
            confirm = Confirmar_Email()
            confirm.start(codigo_email)
            self.rl.add_widget(confirm)
        else:
            alerta = Alerta()
            alerta.start("Erro","Houve um erro ao tentar enviar o e-mail, favor tentar novamente!")
            self.rl.add_widget(alerta)
        #_______________________________________________________________________________________________
        try:
            imagem = cv2.imread(self.dir_img)
        except Exception:
            alerta = Alerta()
            alerta.start("Erro","A imagem enviada não é válida")
            self.rl.add_widget(alerta)
            imagem = None
        cadastro = {
            "person":
            {
            "name":self.nome.get_text(),
            "birthday":f"{self.dia_aniversario.get_text()}/{self.mes_aniversario.get_text()}/{self.ano_aniversario.get_text()}",
            "email":self.email.get_text(),
            "password": self.senha.get_text(),
            "photo": serialize(imagem).decode('latin1'),
            "state": self.estado.get_text(),
            "city": self.cidade.get_text()
            },
            "status":{
                "profession": self.profissao.get_text(),
                "university": self.universidade.get_text(),
                "course": self.curso.get_text(),
                "web_site": self.website.get_text(),
                "linkedin": self.linkedin.get_text()
            },
            "route":"cadastro"
        }
        self.cliente.input_mensage(cadastro)
        resposta = self.cliente.get_msg_server()
        if resposta == True:
            alerta = Alerta()
            alerta.start("Sucesso","Cadastro efetuado com sucesso!")
            self.rl.add_widget(alerta)
            self.clear_widgets()
            self.add_widget(self.screenManager.go_to('login')(self.screenManager))
        else:
            alerta = Alerta()
            alerta.start("Erro","Houve um erro ao efetuar o cadastro, favor verificar os campos novamente!")
            self.rl.add_widget(alerta)
    
    def voltar(self):
        self.clear_widgets()
        self.add_widget(self.screenManager.go_to('login')(self.screenManager))