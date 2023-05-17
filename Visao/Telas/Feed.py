from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Bloco import Bloco,BoxImage
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Rolagem import caixaRolagem
from kivy.uix.label import Label
from Visao.Recursos.Text import Text

class TelaFeed(Screen):
    def __init__(self,screenManager,**kw):
        super().__init__(**kw)
        self.screenManager = screenManager
        self.rl = RelativeLayout()

        fundo = BoxImage('retangulo','Imagens/Fundo2.jpg',size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5})
        self.rl.add_widget(fundo)

        # rolagem do feed
        self.feed = caixaRolagem(800,500,{"center_x":0.54,"center_y":0.4},spacing=0.15)
        self.rl.add_widget(self.feed)
        #---------------------------------------------

        logo = BoxImage('retangulo',"Imagens/Logo.png",size_hint=(.25,.2),pos_hint={'center_x':0.12,'center_y':0.94})
        self.rl.add_widget(logo)

        perfil_button = ImageButton(self.inserir_post,"Imagens/foto_perfil.jpg","circulo",size_hint=(0.1,0.1),pos_hint={"center_x":0.94,"center_y":0.94})
        self.rl.add_widget(perfil_button)

        sair_button = ImageButton(self.voltar,"Imagens/sair.png","retangulo",size_hint=(0.2,0.2),pos_hint={"center_x":0.05,"center_y":0.05})
        self.rl.add_widget(sair_button)

        self.add_widget(self.rl)
    
    def voltar(self):
        self.clear_widgets()
        self.add_widget(self.screenManager.go_to('login')(self.screenManager))
    
    def perfil(self): # Ir para a tela de visualizar perfil
        pass

    def inserir_post(self):# Método chamado para inserir um post no feed do usuário
        post = Bloco(0.8,0.8,pos_hint={"center_x":0.5,"center_y":0.79})
        post.setFormat("retangulo_arredondado",(1,1,1,1))

        # inserir informações do post
        foto_perfil = BoxImage('circulo','Imagens/foto_perfil.jpg',size_hint=(.1,.1),pos_hint={'center_x':0.22,'center_y':0.82})
        post.insertWidget(foto_perfil)

        arroba = Label(text=f'@{"Nome do contato"}',color='black',pos_hint={'center_x':0.4,'center_y':0.84},size_hint=(.01,.01))
        post.insertWidget(arroba)

        info_perfil = Label(text=f'{"Profissão"} | {"Universidade"} | {"Curso"}',color='black',pos_hint={'center_x':0.475,'center_y':0.8},size_hint=(.01,.01))
        post.insertWidget(info_perfil)

        curtir_button = PersonalButton(self.post_curtido,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',pos_hint={'center_x':0.32,'center_y':0.2},size_hint=(0.3,0.05),text="Curtir",borderSize=1.5,borderColor=(0,0,0,1))
        post.insertWidget(curtir_button)

        comentar_button = PersonalButton(self.comentar_post,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',argsAction=[post],pos_hint={'center_x':0.68,'center_y':0.2},size_hint=(0.3,0.05),text="Comentar",borderSize=1.5,borderColor=(0,0,0,1))
        post.insertWidget(comentar_button)

        post.freeze_state()
        #-------------------------

        self.feed.add(post)
    
    def post_curtido(self):
        pass

    def comentar_post(self,post:Bloco): # Tem que receber as informações do post (quem enviou o post e os comentarios existentes)
        post.clearWidgets()
        comentario_post = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),100,pos_hint={"center_x":0.47,'center_y':0.2},size_hint=(.6,.07))
        btn_send = ImageButton(self.enviar_comentario_post,"Imagens/btn_send2.png","retangulo",argsAction=[post,comentario_post],size_hint=(.06,.05),pos_hint={"center_x":0.82,'center_y':0.2})
        post.insertWidget(btn_send)
        post.insertWidget(comentario_post)
        btnVoltar = ImageButton(post.go_to_freeze_state,"Imagens/Voltar.png","circulo",pos_hint={'center_x':0.15,'center_y':0.82},size_hint=(0.05,0.05))
        post.insertWidget(btnVoltar)

        # inserir aqui os comentarios (Precisa criar um bloco rolavel)

        #-----------------------------
    
    def enviar_comentario_post(self,post:Bloco,comentario:Text):# Tem que receber as informações do post para poder enviar o comentario, assim como quem fez o comentario
        if len(comentario.get_text()) > 0:
            foto_perfil = BoxImage('circulo','Imagens/foto_perfil.jpg',size_hint=(.05,.05),pos_hint={'center_x':0.22,'center_y':0.82})
            post.insertWidget(foto_perfil)

            comentLabel = Label(text=f'{comentario.get_text()}',color='black',pos_hint={'center_x':0.4,'center_y':0.82},size_hint=(.01,.01))
            post.insertWidget(comentLabel)