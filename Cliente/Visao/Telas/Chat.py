from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Bloco import Bloco
from Visao.Recursos.Bloco import BoxImage
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Popup import Alerta
from Visao.Recursos.Text import Text
from Visao.Recursos.mensagemChat import Mensagem
from kivy.uix.label import Label
from Visao.Recursos.Rolagem import BlocoRolavel
from random import randint
from Modelo.user import User, create_image_perfil
from Visao.Recursos.Text import TextToSearch
from Comunication.cliente import Cliente
from Visao.Recursos.Rolagem import caixaRolagem

class TelaChat(Screen):
    def __init__(self,screenManager,user:User,**kw):
        super().__init__(**kw)
        self.rl = RelativeLayout()
        self.user = user
        self.contato_img = None
        self.nome_contato = None
        self.contato = None
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

        imgChat = BoxImage('retangulo','Imagens/Fundo_chat.png',size_hint=(.563,.7),pos_hint={'center_x':0.669,'center_y':0.5})
        self.caixaChat.insertWidget(imgChat)

        imgChat2 = BoxImage('retangulo','Imagens/Fundo2.png',size_hint=(.555,.5),pos_hint={'center_x':0.669,'center_y':0.5})
        self.caixaChat.insertWidget(imgChat2)


        self.chat = BlocoRolavel(400,250,pos_hint={'center_x':0.67,'center_y':0.5})

        btn_send = ImageButton(self.enviarMSG,"Imagens/btn_send.png","circulo",size_hint=(.2,.2),pos_hint={"center_x":0.9,'center_y':0.2})
        self.caixaChat.insertWidget(btn_send)

        self.mensagem = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),50,pos_hint={"center_x":0.63,'center_y':0.2},size_hint=(.467,.05))
        self.caixaChat.insertWidget(self.mensagem)

        btnVoltar = PersonalButton(self.voltar,(1,1,1,1),(0,0,0,1),15,"retangulo_arredondado",borderSize=1.2,borderColor=(0,0,0,1),pos_hint={'center_x':0.2,'center_y':0.06},size_hint=(.3,.05),text='Voltar')

        # código copiado do feed de buscar usuário
        # Usar esse código para pegar os amigos e criar os botões para abrir o chat
        btns_search = caixaRolagem(300,200,{"center_x":0.35,"center_y":0.45},spacing=0.91)
        self.caixaChat.insertWidget(btns_search)

        self.cliente.input_mensage({"route":"friends","id":self.user.get_id()})
        self.friends = self.cliente.get_msg_server()
        nomes = [person['name'] for person in self.friends]
        busca = TextToSearch((1,1,1,1),(0,0,0,1),15,(0,0,0,1),nomes,btns_search,self.action_name_search,pos_hint={"center_x":0.22,'center_y':0.2},size_hint=(.3,.05))
        busca.set_defeault_text("Digite o nome do amigo")
        busca.set_new_width_button(1)
        self.caixaChat.insertWidget(busca)
        #--------------------------------------------------------------


        self.rl.add_widget(self.caixaChat)
        self.rl.add_widget(btnVoltar)
        self.rl.add_widget(self.chat)
        self.add_widget(self.rl)
    
    def action_name_search(self,nome):
        if self.contato_img:
            self.caixaChat.removeWidget(self.contato_img)
            self.caixaChat.removeWidget(self.nome_contato)
            self.caixaChat.removeWidget(self.btn_atualizar)
            self.contato_img = None
            self.nome_contato = None
            
        contato = None
        for friend in self.friends:
            if friend['name'] == nome:
                contato = friend
                break
        
        self.go_to_chat(contato)
    
    def atualizar_chat(self,contato):
        self.chat.clearWidgets()
        self.cliente.input_mensage({'route':'recive_msg','author':contato['id'],'destine':self.user.get_id()})
        mensagens_recived = self.cliente.get_msg_server()

        self.cliente.input_mensage({'route':'recive_msg','author':self.user.get_id(),'destine':contato['id']})
        mensagens_sended = self.cliente.get_msg_server()

        self.mensagens = sorted([*mensagens_recived,*mensagens_sended],key=lambda x: x['date'])
        for mensagem in self.mensagens:
            msg = Mensagem(mensagem['text'],15,mensagem['author_id']==self.user.get_id(),size_hint=(.2,.05))
            self.chat.add(msg)

    def go_to_chat(self,contato):
        self.chat.clearWidgets()
        self.contato = contato
        self.btn_atualizar = ImageButton(self.atualizar_chat,"Imagens/atualizar_btn.png","circulo",argsAction=[contato],pos_hint={'center_x':0.8,'center_y':0.8},size_hint=(0.04,0.04))
        self.caixaChat.insertWidget(self.btn_atualizar)
        path_foto_user = f"temp/user_see_chat_{contato['name']}.png"
        path_foto_user = create_image_perfil(path_foto_user,contato['photo'])

        self.contato_img = BoxImage("circulo",path_foto_user,pos_hint={'center_x':0.45,'center_y':0.8},size_hint=(0.07,0.07))
        self.nome_contato = Label(text=contato['name'],color='white',pos_hint={'center_x':0.57,'center_y':0.8},size_hint=(.04,.02))
    
        self.caixaChat.insertWidget(self.contato_img)
        self.caixaChat.insertWidget(self.nome_contato)

        self.cliente.input_mensage({'route':'recive_msg','author':contato['id'],'destine':self.user.get_id()})
        mensagens_recived = self.cliente.get_msg_server()

        self.cliente.input_mensage({'route':'recive_msg','author':self.user.get_id(),'destine':contato['id']})
        mensagens_sended = self.cliente.get_msg_server()

        self.mensagens = sorted([*mensagens_recived,*mensagens_sended],key=lambda x: x['date'])
        for mensagem in self.mensagens:
            msg = Mensagem(mensagem['text'],15,mensagem['author_id']==self.user.get_id(),size_hint=(.2,.05))
            self.chat.add(msg)        
    
    def voltar(self):
        self.thread_chat = False
        self.clear_widgets()
        self.add_widget(self.screenManager.go_to('feed')(self.screenManager,self.user))

    def enviarMSG(self):
        texto = self.mensagem.get_text()
        self.cliente.input_mensage({'route':"send_msg",'id_envio':self.user.get_id(),'id_recebe':self.contato['id'],'text':texto})
        sucesso = self.cliente.get_msg_server()
        if not sucesso:
            alerta = Alerta()
            alerta.start("Erro","A mensagem não pôde ser enviada, favor tentar novamente!")
            self.rl.add_widget(alerta)
        else:
            self.atualizar_chat(self.contato)