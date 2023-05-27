from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Bloco import Bloco
from Visao.Recursos.Bloco import BoxImage
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Text import Text
from Visao.Recursos.mensagemChat import Mensagem
from kivy.uix.label import Label
from Visao.Recursos.Rolagem import BlocoRolavel
from random import randint
from Modelo.user import User
from Visao.Recursos.Text import TextToSearch
from Comunication.cliente import Cliente
from Visao.Recursos.Rolagem import caixaRolagem

class TelaChat(Screen):
    def __init__(self,screenManager,user:User,**kw):
        super().__init__(**kw)
        self.rl = RelativeLayout()
        self.user = user
        self.screenManager = screenManager
        self.cliente:Cliente = screenManager.get_client()
        fundo = BoxImage('retangulo','Imagens/Fundo2.jpg',size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5})
        self.rl.add_widget(fundo)
        logo = BoxImage('retangulo',"Imagens/Logo.png",size_hint=(.25,.2),pos_hint={'center_x':0.17,'center_y':0.945})
        self.rl.add_widget(logo)

        self.caixaChat = Bloco(0.7,0.9,pos_hint={'center_x':0.5,'center_y':0.5})
        self.caixaChat.setFormat("retangulo_arredondado",(1,1,1,1),borderSize=2,borderColor=(0,0,0,1))

        imgUser = BoxImage("circulo",self.user.get_path_image(),pos_hint={'center_x':0.2,'center_y':0.84},size_hint=(0.15,0.15))
        self.caixaChat.insertWidget(imgUser)

        nomeUser = Label(text=f'{self.user.get_nome()}',color='black',pos_hint={'center_x':0.2,'center_y':0.75},size_hint=(.06,.02))
        self.caixaChat.insertWidget(nomeUser)

        imgChat = BoxImage('retangulo','Imagens/Fundo_chat.png',size_hint=(.565,.7),pos_hint={'center_x':0.669,'center_y':0.5})
        self.caixaChat.insertWidget(imgChat)

        contato = BoxImage("circulo",'Imagens/foto_perfil.jpg',pos_hint={'center_x':0.45,'center_y':0.8},size_hint=(0.07,0.07))
        nome_contato = Label(text='Nome do contato',color='white',pos_hint={'center_x':0.57,'center_y':0.82},size_hint=(.04,.02))
        profissao = Label(text='Profissão',color='white',pos_hint={'center_x':0.57,'center_y':0.79},size_hint=(.04,.02))
        self.caixaChat.insertWidget(profissao)
        self.caixaChat.insertWidget(nome_contato)
        self.caixaChat.insertWidget(contato)

        self.chat = BlocoRolavel(400,250,pos_hint={'center_x':0.67,'center_y':0.5})

        btn_send = ImageButton(self.enviarMSG,"Imagens/btn_send.png","circulo",size_hint=(.2,.2),pos_hint={"center_x":0.9,'center_y':0.2})
        self.caixaChat.insertWidget(btn_send)

        self.mensagem = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),50,pos_hint={"center_x":0.63,'center_y':0.2},size_hint=(.467,.05))
        self.caixaChat.insertWidget(self.mensagem)

        btnVoltar = PersonalButton(self.voltar,(1,1,1,1),(0,0,0,1),15,"retangulo_arredondado",borderSize=1.2,borderColor=(0,0,0,1),pos_hint={'center_x':0.2,'center_y':0.06},size_hint=(.3,.05),text='Voltar')

        # código copiado do feed de buscar usuário
        # Usar esse código para pegar os amigos e criar os botões para abrir o chat
        btns_search = caixaRolagem(500,200,{"center_x":0.5,"center_y":0.45},spacing=0.91)
        self.search_user.insertWidget(btns_search)

        self.cliente.input_mensage({"route":"friends"})
        self.friends = self.cliente.get_msg_server()
        nomes = [person['name'] for person in self.persons]
        busca = TextToSearch((1,1,1,1),(0,0,0,1),15,(0,0,0,1),nomes,btns_search,self.action_name_search,pos_hint={"center_x":0.5,'center_y':0.7},size_hint=(.5,.05))
        self.search_user.insertWidget(busca)
        self.rl.add_widget(self.search_user)
        #--------------------------------------------------------------

        self.rl.add_widget(self.caixaChat)
        self.rl.add_widget(btnVoltar)
        self.rl.add_widget(self.chat)
        self.add_widget(self.rl)
    
    def action_name_search(self,nome):
        pass

    def voltar(self):
        self.clear_widgets()
        self.add_widget(self.screenManager.go_to('feed')(self.screenManager,self.user))

    def enviarMSG(self):
        texto = self.mensagem.get_text()
        # label = Label(text=texto,color='black',size_hint=(.467,.05),pos=[50,50])
        teste = [True,False]
        mensagem = Mensagem(texto,15,teste[randint(0,1)],size_hint=(.2,.05))
        self.chat.add(mensagem)