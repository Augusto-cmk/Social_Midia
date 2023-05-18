from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Bloco import BoxImage,Post,Bloco,Projeto
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Geometry import Geometry
from Visao.Recursos.Rolagem import caixaRolagem
from kivy.uix.label import Label
from Visao.Recursos.Text import Text,TextToSearch
from Visao.Recursos.choose_file import Choose_file

class TelaFeed(Screen):
    def __init__(self,screenManager,**kw):
        super().__init__(**kw)
        self.screenManager = screenManager
        self.rl = RelativeLayout()

        fundo = BoxImage('retangulo','Imagens/Fundo2.jpg',size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5})
        self.rl.add_widget(fundo)

        # rolagem do feed
        self.feed = caixaRolagem(800,500,{"center_x":0.5,"center_y":0.45},spacing=0.15)
        self.rl.add_widget(self.feed)
        #---------------------------------------------

        logo = BoxImage('retangulo',"Imagens/Logo.png",size_hint=(.25,.2),pos_hint={'center_x':0.12,'center_y':0.94})
        self.rl.add_widget(logo)

        path_foto_perfil = "Imagens/foto_perfil.jpg"
        nome = "Pedro Maia"
        colaboradores = 192
        colaborando = 53
        perfil_button = ImageButton(self.perfil,"Imagens/foto_perfil.jpg","circulo",argsAction=[path_foto_perfil,nome,colaboradores,colaborando],size_hint=(0.1,0.1),pos_hint={"center_x":0.94,"center_y":0.94})
        self.rl.add_widget(perfil_button)

        self.sair_button = ImageButton(self.voltar,"Imagens/sair.png","retangulo",size_hint=(0.2,0.2),pos_hint={"center_x":0.05,"center_y":0.05})
        self.rl.add_widget(self.sair_button)

        self.post_btn = ImageButton(self.criar_post,"Imagens/CriarPost.png","circulo",size_hint=(0.27,0.25),pos_hint={"center_x":0.94,"center_y":0.70})
        self.rl.add_widget(self.post_btn)

        self.search_btn = ImageButton(self.buscar_usuario,"Imagens/BuscarUsuario.png","circulo",size_hint=(0.27,0.27),pos_hint={"center_x":0.94,"center_y":0.46})
        self.rl.add_widget(self.search_btn)

        self.add_widget(self.rl)
        self.postagem = None
        self.search_user = None
        self.perfil_user = None

    def buscar_usuario(self): # Cria um bloco para buscar um novo usuário (Enquanto digita, vão aparecendo os botões de sujestão)
        self.rl.remove_widget(self.feed)
        if self.search_user:
            self.rl.remove_widget(self.search_user)
            self.search_user = None
        
        if self.postagem:
            self.rl.remove_widget(self.postagem)
            self.postagem = None
        
        if self.perfil_user:
            self.rl.remove_widget(self.perfil_user)
            self.perfil_user = None
        
        self.search_user = Bloco(0.75,0.75,pos_hint={"center_x":0.5,"center_y":0.5})
        self.search_user.setFormat("retangulo_arredondado",(1,1,1,1))

        cancelar = PersonalButton(self.restore_to_feed,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',pos_hint={'center_x':0.5,'center_y':0.2},size_hint=(0.3,0.05),text="Cancelar",borderSize=1.5,borderColor=(0,0,0,1))
        self.search_user.insertWidget(cancelar)

        btns_search = caixaRolagem(500,200,{"center_x":0.5,"center_y":0.45},spacing=0.91)
        self.search_user.insertWidget(btns_search)

        label = Label(text="Pesquise por um usuário para colaboração",color='black',pos_hint={'center_x':0.5,'center_y':0.82},size_hint=(.01,.01))
        self.search_user.insertWidget(label)

        busca = TextToSearch((1,1,1,1),(0,0,0,1),15,(0,0,0,1),["Pedro","Patrick","Pietro","Victoria","Gabriel"],btns_search,self.action_name_search,pos_hint={"center_x":0.5,'center_y':0.7},size_hint=(.5,.05))
        self.search_user.insertWidget(busca)

        self.rl.add_widget(self.search_user)

    def action_name_search(self,nome):# O nome vai ser a chave de um dicionário que contém as informações do usuário selecionado,ao entrar nesse método, o nome selecionado vai ser obtido e podemos acessar as informações pelo dicionario e ir para o perfil desse usuário
        print(nome) 

    def criar_post(self): # Aqui vai dar um self.r.remove_widget(self.feed) e depois abrir um bloco para criar um post
        self.rl.remove_widget(self.feed)

        if self.search_user:
            self.rl.remove_widget(self.search_user)
            self.search_user = None
        
        if self.postagem:
            self.rl.remove_widget(self.postagem)
            self.postagem = None
        
        if self.perfil_user:
            self.rl.remove_widget(self.perfil_user)
            self.perfil_user = None
        
        self.postagem = Bloco(0.7,0.7,pos_hint={"center_x":0.5,"center_y":0.5})
        self.postagem.setFormat("retangulo_arredondado",(1,1,1,1))
        
        path_foto_perfil = "Imagens/foto_perfil.jpg"
        nome_autor = "Pedro Maia"
        
        label = Label(text="Insira aqui a descrição da postagem (40 caracteres)",color='black',pos_hint={'center_x':0.5,'center_y':0.82},size_hint=(.01,.01))
        text_post = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),40,pos_hint={"center_x":0.5,'center_y':0.77},size_hint=(.6,.07))

        path_image_post = dict()
        self.insert_image = ImageButton(self.inserir_image_post,"Imagens/search_image.png","retangulo",argsAction=[path_image_post],pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.3,0.3))

        publicar = PersonalButton(self.inserir_post,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',
                                  argsAction=[path_foto_perfil,nome_autor,text_post,path_image_post],pos_hint={'center_x':0.68,'center_y':0.2},size_hint=(0.3,0.05),text="Publicar",borderSize=1.5,borderColor=(0,0,0,1))
        
        cancelar = PersonalButton(self.restore_to_feed,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',pos_hint={'center_x':0.32,'center_y':0.2},size_hint=(0.3,0.05),text="Cancelar",borderSize=1.5,borderColor=(0,0,0,1))
        
        self.postagem.insertWidget(label)
        self.postagem.insertWidget(text_post)
        self.postagem.insertWidget(publicar)
        self.postagem.insertWidget(cancelar)
        self.postagem.insertWidget(self.insert_image)
        self.rl.add_widget(self.postagem)
    
    def inserir_image_post(self,path:dict):
        path['path'] = Choose_file().get_dir()
        self.postagem.removeWidget(self.insert_image)
        image = BoxImage('retangulo',path['path'],size_hint=(.6,.35),pos_hint={'center_x':0.5,'center_y':0.5})
        self.postagem.insertWidget(image)


    def restore_to_feed(self):
        if self.postagem:
            self.rl.remove_widget(self.postagem)
        
        if self.search_user:
            self.rl.remove_widget(self.search_user)
        
        if self.perfil_user:
            self.rl.remove_widget(self.perfil_user)
        
        self.rl.remove_widget(self.post_btn)
        self.rl.remove_widget(self.sair_button)
        self.rl.remove_widget(self.search_btn)
        self.rl.add_widget(self.feed)
        self.rl.add_widget(self.post_btn)
        self.rl.add_widget(self.sair_button)
        self.rl.add_widget(self.search_btn)

    def voltar(self):
        self.clear_widgets()
        self.add_widget(self.screenManager.go_to('login')(self.screenManager))
    
    def perfil(self,path_foto_perfil,nome,colabs,colab): # Criar um bloco para visualizar o perfil
        self.rl.remove_widget(self.feed)
        if self.search_user:
            self.rl.remove_widget(self.search_user)
            self.search_user = None
        
        if self.postagem:
            self.rl.remove_widget(self.postagem)
            self.postagem = None
        
        if self.perfil_user:
            self.rl.remove_widget(self.perfil_user)
            self.perfil_user = None
        
        self.perfil_user = Bloco(0.75,0.75,pos_hint={"center_x":0.5,"center_y":0.5})
        self.perfil_user.setFormat("retangulo_arredondado",(1,1,1,1))
        
        btnVoltar = ImageButton(self.restore_to_feed,"Imagens/Voltar.png","circulo",pos_hint={'center_x':0.16,'center_y':0.84},size_hint=(0.05,0.05))
        self.perfil_user.insertWidget(btnVoltar)

        foto_perfil = BoxImage('circulo',path_foto_perfil,size_hint=(.1,.1),pos_hint={'center_x':0.22,'center_y':0.78})
        self.perfil_user.insertWidget(foto_perfil)

        colaboradores = Label(text="colaboradores",color='black',pos_hint={'center_x':0.44,'center_y':0.75},size_hint=(.01,.01))
        self.perfil_user.insertWidget(colaboradores)

        colaborando = Label(text="colaborando",color='black',pos_hint={'center_x':0.7,'center_y':0.75},size_hint=(.01,.01))
        self.perfil_user.insertWidget(colaborando)

        colaboradoresSize = Label(text=f"{colabs}",color='black',pos_hint={'center_x':0.44,'center_y':0.78},size_hint=(.01,.01))
        self.perfil_user.insertWidget(colaboradoresSize)

        colaborandoSize = Label(text=f"{colab}",color='black',pos_hint={'center_x':0.7,'center_y':0.78},size_hint=(.01,.01))
        self.perfil_user.insertWidget(colaborandoSize)

        nomePerfil = Label(text=nome,color='black',pos_hint={'center_x':0.22,'center_y':0.7},size_hint=(.01,.01))
        self.perfil_user.insertWidget(nomePerfil)

        editar_btn = PersonalButton(self.editar_perfil,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',pos_hint={'center_x':0.5,'center_y':0.65},size_hint=(0.4,0.05),text="Editar Perfil",borderSize=1.5,borderColor=(0,0,0,1))
        self.perfil_user.insertWidget(editar_btn)
        
        projetos = caixaRolagem(600,250,{"center_x":0.5,"center_y":0.45},spacing=0.2)
        self.perfil_user.insertWidget(projetos)

        paths = ["Imagens/ForgotSenha.png","Imagens/Fundo_chat.png","Imagens/OlhoFechado.png"]
        for path in paths:
            project = Projeto(0.7,0.7,{"center_x":0.5,"center_y":0.8},path,153,20)
            project.show()
            projetos.add(project)

        self.rl.add_widget(self.perfil_user)
    
    def editar_perfil(self):
        pass

    def inserir_post(self,path_foto_perfil,nome_autor,text_post:Text,path_image_post:dict):# Método chamado para inserir um post no feed do usuário
        do = True
        if self.postagem:
            try:
                path_image_post['path']
                self.restore_to_feed()
                self.postagem = None
            except Exception:
                do = False
        
        if do:
            post = Post(0.8,0.8,pos_hint={"center_x":0.5,"center_y":0.79})
            post.setFormat("retangulo_arredondado",(1,1,1,1))

            # inserir informações do post
            foto_perfil = BoxImage('circulo',path_foto_perfil,size_hint=(.1,.1),pos_hint={'center_x':0.22,'center_y':0.82})
            post.insertWidget(foto_perfil)

            arroba = Label(text=f'@{nome_autor}',color='black',pos_hint={'center_x':0.4,'center_y':0.82},size_hint=(.01,.01))
            post.insertWidget(arroba)

            separador = Geometry('retangulo',(0,0,0,0.2),pos_hint={'center_x':0.5,'center_y':0.75},size_hint=(.8,.003))

            post.insertWidget(separador)

            text_post = Label(text=text_post.get_text(),color='black',pos_hint={'center_x':0.5,'center_y':0.7},size_hint=(.01,.01))
            post.insertWidget(text_post)

            img_post = BoxImage('retangulo',path_image_post['path'],size_hint=(.6,.35),pos_hint={'center_x':0.5,'center_y':0.45})
            post.insertWidget(img_post)

            curtir_button = PersonalButton(self.post_curtido,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',pos_hint={'center_x':0.32,'center_y':0.2},size_hint=(0.3,0.05),text="Curtir",borderSize=1.5,borderColor=(0,0,0,1))
            post.insertWidget(curtir_button)

            comentar_button = PersonalButton(self.comentar_post,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',argsAction=[post],pos_hint={'center_x':0.68,'center_y':0.2},size_hint=(0.3,0.05),text="Comentar",borderSize=1.5,borderColor=(0,0,0,1))
            post.insertWidget(comentar_button)

            post.freeze_state()
            #-------------------------

            self.feed.add(post)
        
    def post_curtido(self):
        pass

    def comentar_post(self,post:Post): # Tem que receber as informações do post (quem enviou o post e os comentarios existentes)
        post.clearWidgets()
        comentario_post = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),35,pos_hint={"center_x":0.47,'center_y':0.2},size_hint=(.6,.07))
        btn_send = ImageButton(self.enviar_comentario_post,"Imagens/btn_send2.png","retangulo",argsAction=[post,comentario_post],size_hint=(.06,.05),pos_hint={"center_x":0.82,'center_y':0.2})
        post.insertWidget(btn_send)
        post.insertWidget(comentario_post)
        btnVoltar = ImageButton(post.go_to_freeze_state,"Imagens/Voltar.png","circulo",pos_hint={'center_x':0.15,'center_y':0.82},size_hint=(0.05,0.05))
        post.insertWidget(btnVoltar)
        # inserir aqui os comentarios (Precisa criar um bloco rolavel)

        #-----------------------------
    
    def enviar_comentario_post(self,post:Post,comentario:Text):# Tem que receber as informações do post para poder enviar o comentario, assim como quem fez o comentario
        if len(comentario.get_text()) > 0:
            foto_perfil = BoxImage('circulo','Imagens/foto_perfil.jpg',size_hint=(.05,.05),pos_hint={'center_x':0.22,'center_y':0.82})
            comentLabel = Label(text=f'{comentario.get_text()}',color='black',pos_hint={'center_x':0.5,'center_y':0.82},size_hint=(.01,.01))
            post.comment(foto_perfil,comentLabel)