import os
from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Bloco import BoxImage,Post,Bloco,Projeto
from Visao.Recursos.Botao import PersonalButton,ImageButton
from Visao.Recursos.Geometry import Geometry
from Visao.Recursos.Rolagem import caixaRolagem
from kivy.uix.label import Label
from Visao.Recursos.Text import Text,TextToSearch
from Visao.Recursos.checkbox import Interactive_Checkbox
from Visao.Recursos.choose_file import Choose_file
from Modelo.user import User, create_image_perfil
from cv2 import imread
from Comunication.mensagem import serialize
from Visao.Recursos.Popup import Alerta
from Comunication.cliente import Client
import datetime


class TelaFeed(Screen):
    def __init__(self,screenManager,user:User,**kw):
        super().__init__(**kw)
        self.screenManager = screenManager
        self.cliente:Client = self.screenManager.get_client()
        self.user = user
        self.rl = RelativeLayout()

        fundo = BoxImage('retangulo','Imagens/Fundo2.jpg',size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.5})
        self.rl.add_widget(fundo)

        # rolagem do feed
        self.feed = caixaRolagem(800,500,{"center_x":0.5,"center_y":0.45},spacing=0.15)
        self.rl.add_widget(self.feed)
        #---------------------------------------------

        logo = BoxImage('retangulo',"Imagens/Logo.png",size_hint=(.25,.2),pos_hint={'center_x':0.12,'center_y':0.94})
        self.rl.add_widget(logo)

        self.perfil_button = ImageButton(self.perfil,self.user.get_path_image(),"circulo",size_hint=(0.1,0.1),pos_hint={"center_x":0.94,"center_y":0.94})
        self.rl.add_widget(self.perfil_button)

        self.sair_button = ImageButton(self.voltar,"Imagens/sair.png","retangulo",size_hint=(0.2,0.2),pos_hint={"center_x":0.05,"center_y":0.05})
        self.rl.add_widget(self.sair_button)

        self.post_btn = ImageButton(self.criar_post,"Imagens/CriarPost.png","circulo",size_hint=(0.27,0.25),pos_hint={"center_x":0.94,"center_y":0.70})
        self.rl.add_widget(self.post_btn)

        self.search_btn = ImageButton(self.buscar_usuario,"Imagens/BuscarUsuario.png","circulo",size_hint=(0.27,0.27),pos_hint={"center_x":0.94,"center_y":0.46})
        self.rl.add_widget(self.search_btn)

        self.chat_btn = ImageButton(self.chat,"Imagens/btn_chat.png","circulo",size_hint=(0.22,0.22),pos_hint={"center_x":0.94,"center_y":0.22})
        self.rl.add_widget(self.chat_btn)

        self.atualizar_btn = ImageButton(self.atualizar_feed,"Imagens/atualizar_btn.png","circulo",size_hint=(0.1,0.1),pos_hint={"center_x":0.5,"center_y":0.93})
        self.rl.add_widget(self.atualizar_btn)

        self.postagem = None
        self.search_user = None
        self.perfil_user = None
        self.editarPerfil = None
        self.dir_img = None
        ## método para obter o feed do banco de dados
        self.atualizar_feed()
        #---------------------------------------------------------------------------------------------------
        self.add_widget(self.rl)
    
    def chat(self):
        self.clear_widgets()
        self.add_widget(self.screenManager.go_to('chat')(self.screenManager,self.user))

    def atualizar_feed(self):
        self.feed.clear()
        amigos = self.cliente.person_service.get_friends_person(self.user.get_id())
        for amigo in amigos:
            posts = self.cliente.post_service.get_posts(amigo['id'])
            i = 0
            path_perfil = create_image_perfil(f"temp/post_perfil_{amigo['name']}.png",amigo['photo'])
            for j,post in enumerate(posts):
                path = {}
                path['path'] = create_image_perfil(f"temp/post_{amigo['name']}_{i}_{j}.png",post['image'])
                comentarios = len(self.cliente.post_service.get_comments(post['id']))
                self.inserir_post_friends(post['id'],post['curtir'],comentarios,post['text'],path,amigo['name'],path_perfil)
        
        my_posts = self.cliente.post_service.get_posts(self.user.get_id())
        for i,my_post in enumerate(my_posts):
            path = {}
            path['path'] = create_image_perfil(f"temp/post_{self.user.get_nome()}_{i}.png",my_post['image'])
            comentarios = len(self.cliente.post_service.get_comments(my_post['id']))
            self.inserir_post_friends(my_post['id'],my_post['curtir'],comentarios,my_post['text'],path,self.user.get_nome(),self.user.get_path_image())

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
        
        if self.editarPerfil:
            self.rl.remove_widget(self.editarPerfil)
            self.editarPerfil = None
        
        
        self.search_user = Bloco(0.75,0.75,pos_hint={"center_x":0.5,"center_y":0.5})
        self.search_user.setFormat("retangulo_arredondado",(1,1,1,1))

        cancelar = PersonalButton(self.restore_to_feed,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',pos_hint={'center_x':0.5,'center_y':0.2},size_hint=(0.3,0.05),text="Cancelar",borderSize=1.5,borderColor=(0,0,0,1))
        self.search_user.insertWidget(cancelar)

        btns_search = caixaRolagem(500,200,{"center_x":0.5,"center_y":0.45},spacing=0.91)
        self.search_user.insertWidget(btns_search)

        label = Label(text="Pesquise por um usuário para colaboração",color='black',pos_hint={'center_x':0.5,'center_y':0.82},size_hint=(.01,.01))
        self.search_user.insertWidget(label)
        
        self.persons = self.cliente.person_service.get_persons_all()
        nomes = [person['name'] for person in self.persons]
        busca = TextToSearch((1,1,1,1),(0,0,0,1),15,(0,0,0,1),nomes,btns_search,self.action_name_search,pos_hint={"center_x":0.5,'center_y':0.7},size_hint=(.5,.05))
        self.search_user.insertWidget(busca)

        self.rl.add_widget(self.search_user)

    def action_name_search(self, nome):# O nome vai ser a chave de um dicionário que contém as informações do usuário selecionado,ao entrar nesse método, o nome selecionado vai ser obtido e podemos acessar as informações pelo dicionario e ir para o perfil desse usuário
        for person in self.persons:
            if person['name'] == nome:
                perfil = person
                break
        
        perfil = self.cliente.person_service.get_person(perfil['id'])
        self.visualizar_perfil_usuario(perfil)

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

        if self.editarPerfil:
            self.rl.remove_widget(self.editarPerfil)
            self.editarPerfil = None
        
        self.postagem = Bloco(0.7,0.7,pos_hint={"center_x":0.5,"center_y":0.5})
        self.postagem.setFormat("retangulo_arredondado",(1,1,1,1))
    
        
        label = Label(text="Insira aqui a descrição da postagem (40 caracteres)",color='black',pos_hint={'center_x':0.5,'center_y':0.82},size_hint=(.01,.01))
        text_post = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),40,pos_hint={"center_x":0.5,'center_y':0.77},size_hint=(.6,.07))

        path_image_post = dict()
        self.insert_image = ImageButton(self.inserir_image_post,"Imagens/search_image.png","retangulo",argsAction=[path_image_post],pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.3,0.3))

        publicar = PersonalButton(self.inserir_post,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',
                                  argsAction=[text_post,path_image_post],pos_hint={'center_x':0.68,'center_y':0.2},size_hint=(0.3,0.05),text="Publicar",borderSize=1.5,borderColor=(0,0,0,1))
        
        cancelar = PersonalButton(self.restore_to_feed,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',pos_hint={'center_x':0.32,'center_y':0.2},size_hint=(0.3,0.05),text="Cancelar",borderSize=1.5,borderColor=(0,0,0,1))
        
        self.postagem.insertWidget(label)
        self.postagem.insertWidget(text_post)
        self.postagem.insertWidget(publicar)
        self.postagem.insertWidget(cancelar)
        self.postagem.insertWidget(self.insert_image)
        self.rl.add_widget(self.postagem)
    
    def inserir_image_post(self,path:dict):
        path['path'] = Choose_file().get_dir()
        if path['path'] != ():
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
        self.rl.remove_widget(self.chat_btn)
        self.rl.add_widget(self.feed)
        self.rl.add_widget(self.post_btn)
        self.rl.add_widget(self.sair_button)
        self.rl.add_widget(self.search_btn)
        self.rl.add_widget(self.chat_btn)

    def voltar(self):
        arquivos = os.listdir("temp")
        for arquivo in arquivos:
            os.remove(f"temp/{arquivo}")

        self.clear_widgets()
        self.add_widget(self.screenManager.go_to('login')(self.screenManager))
    
    def colaborar(self, id_perfil): # Local onde o usuário passa a ser colaborador do perfil visualizado
        resposta = self.cliente.friend_service.create_friends(self.user.get_id(),id_perfil)
        if resposta:
            self.user.set_colaborando(self.user.get_colaborando()+1)
            self.colaboradoresSize.text = str(int(self.colaboradoresSize.text)+1)
            self.perfil_user.removeWidget(self.colaborar_btn)
            self.colaborar_btn = PersonalButton(self.desfazer_colaboracao,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',argsAction=[id_perfil],pos_hint={'center_x':0.5,'center_y':0.69},size_hint=(0.4,0.05),text="Deixar de colaborar",borderSize=1.5,borderColor=(0,0,0,1))
            self.perfil_user.insertWidget(self.colaborar_btn)
                    
        
    def desfazer_colaboracao(self,id_perfil): # Precisa implementar esse método 
        resposta = self.cliente.friend_service.delete_friends(self.user.get_id(),id_perfil)
        if resposta:
            self.user.set_colaborando(self.user.get_colaborando()-1)
            self.colaboradoresSize.text = str(int(self.colaboradoresSize.text)-1)
            self.perfil_user.removeWidget(self.colaborar_btn)
            self.colaborar_btn = PersonalButton(self.colaborar,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',argsAction=[id_perfil],pos_hint={'center_x':0.5,'center_y':0.69},size_hint=(0.4,0.05),text="Colaborar",borderSize=1.5,borderColor=(0,0,0,1))
            self.perfil_user.insertWidget(self.colaborar_btn)

    def visualizar_perfil_usuario(self, perfil):
        if int(self.user.get_id()) == int(perfil['id']):
            self.perfil()
        else:
            self.rl.remove_widget(self.feed)
            status_perfil = self.cliente.person_status_service.get_person_status(perfil['id'])

            already_colaborando = perfil['id'] in [friend['id'] for friend in self.cliente.person_service.get_friends_person(self.user.get_id())]

            if self.search_user:
                self.rl.remove_widget(self.search_user)
                self.search_user = None
            
            if self.postagem:
                self.rl.remove_widget(self.postagem)
                self.postagem = None
            
            if self.perfil_user:
                self.rl.remove_widget(self.perfil_user)
                self.perfil_user = None
            
            if self.editarPerfil:
                self.rl.remove_widget(self.editarPerfil)
                self.editarPerfil = None
            
            self.perfil_user = Bloco(0.85,0.75,pos_hint={"center_x":0.5,"center_y":0.47})
            self.perfil_user.setFormat("retangulo_arredondado",(1,1,1,1))
            
            btnVoltar = ImageButton(self.restore_to_feed,"Imagens/Voltar.png","circulo",pos_hint={'center_x':0.16,'center_y':0.88},size_hint=(0.05,0.05))
            self.perfil_user.insertWidget(btnVoltar)

            path_foto_user = f"temp/user_see_{perfil['name']}.png"
            path_foto_user = create_image_perfil(path_foto_user,perfil['photo'])

            foto_perfil = BoxImage('circulo',path_foto_user,size_hint=(.1,.1),pos_hint={'center_x':0.22,'center_y':0.82})
            self.perfil_user.insertWidget(foto_perfil)

            colaboradores = Label(text="colaboradores",color='black',pos_hint={'center_x':0.44,'center_y':0.79},size_hint=(.01,.01))
            self.perfil_user.insertWidget(colaboradores)

            colaborando = Label(text="colaborando",color='black',pos_hint={'center_x':0.7,'center_y':0.79},size_hint=(.01,.01))
            self.perfil_user.insertWidget(colaborando)

            # Aplicar a lógica para obter os colaboradores e colaborandos do BD
            colab = self.cliente.person_service.get_len_colaborando(perfil['id'])
            colabs = self.cliente.person_service.get_len_colaborandores(perfil['id'])
            self.colaboradoresSize = Label(text=f"{colabs}",color='black',pos_hint={'center_x':0.44,'center_y':0.82},size_hint=(.01,.01))
            self.perfil_user.insertWidget(self.colaboradoresSize)

            colaborandoSize = Label(text=f"{colab}",color='black',pos_hint={'center_x':0.7,'center_y':0.82},size_hint=(.01,.01))
            self.perfil_user.insertWidget(colaborandoSize)

            nomePerfil = Label(text=perfil['name'],color='black',pos_hint={'center_x':0.22,'center_y':0.74},size_hint=(.01,.01))
            self.perfil_user.insertWidget(nomePerfil)

            if not already_colaborando:
                self.colaborar_btn = PersonalButton(self.colaborar,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',argsAction=[perfil['id']],pos_hint={'center_x':0.5,'center_y':0.69},size_hint=(0.4,0.05),text="Colaborar",borderSize=1.5,borderColor=(0,0,0,1))
                self.perfil_user.insertWidget(self.colaborar_btn)

            else:
                self.colaborar_btn = PersonalButton(self.desfazer_colaboracao,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',argsAction=[perfil['id']],pos_hint={'center_x':0.5,'center_y':0.69},size_hint=(0.4,0.05),text="Deixar de colaborar",borderSize=1.5,borderColor=(0,0,0,1))
                self.perfil_user.insertWidget(self.colaborar_btn)

            linkedinLabel = Label(text=f"Linkedin: {status_perfil['linkedin']}",color='black',pos_hint={'center_x':0.5,'center_y':0.17},size_hint=(.01,.01))
            emailLabel = Label(text=f"Email: {perfil['email']}",color='black',pos_hint={'center_x':0.5,'center_y':0.14},size_hint=(.01,.01))
            githubLabel = Label(text=f"Web_site: {status_perfil['web_site']}",color='black',pos_hint={'center_x':0.5,'center_y':0.11},size_hint=(.01,.01))

            self.perfil_user.insertWidget(linkedinLabel)
            self.perfil_user.insertWidget(emailLabel)
            self.perfil_user.insertWidget(githubLabel)
            
            # Criar a lógica para pegas os posts do usuário, likes de cada post e comentarios de cada post ( quantidade )
            projetos = caixaRolagem(600,250,{"center_x":0.5,"center_y":0.46},spacing=0.2)
            self.perfil_user.insertWidget(projetos)

            my_posts = self.cliente.post_service.get_posts(perfil['id'])
            for i,my_post in enumerate(my_posts):
                path = create_image_perfil(f"temp/post_{perfil['name']}_{i}.png",my_post['image'])
                comentarios = len(self.cliente.post_service.get_comments(my_post['id']))
                project = Projeto(0.7,0.7,{"center_x":0.5,"center_y":0.8},path,my_post['curtir'],comentarios)
                project.show()
                projetos.add(project)

            self.rl.add_widget(self.perfil_user)
    
    def perfil(self): # Criar um bloco para visualizar o perfil
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
        
        if self.editarPerfil:
            self.rl.remove_widget(self.editarPerfil)
            self.editarPerfil = None
        
        self.perfil_user = Bloco(0.85,0.75,pos_hint={"center_x":0.5,"center_y":0.47})
        self.perfil_user.setFormat("retangulo_arredondado",(1,1,1,1))
        
        btnVoltar = ImageButton(self.restore_to_feed,"Imagens/Voltar.png","circulo",pos_hint={'center_x':0.16,'center_y':0.88},size_hint=(0.05,0.05))
        self.perfil_user.insertWidget(btnVoltar)

        foto_perfil = BoxImage('circulo',self.user.get_path_image(),size_hint=(.1,.1),pos_hint={'center_x':0.22,'center_y':0.82})
        self.perfil_user.insertWidget(foto_perfil)

        colaboradores = Label(text="colaboradores",color='black',pos_hint={'center_x':0.44,'center_y':0.79},size_hint=(.01,.01))
        self.perfil_user.insertWidget(colaboradores)

        colaborando = Label(text="colaborando",color='black',pos_hint={'center_x':0.7,'center_y':0.79},size_hint=(.01,.01))
        self.perfil_user.insertWidget(colaborando)

        colaboradoresSize = Label(text=f"{self.user.get_colaboradores()}",color='black',pos_hint={'center_x':0.44,'center_y':0.82},size_hint=(.01,.01))
        self.perfil_user.insertWidget(colaboradoresSize)

        colaborandoSize = Label(text=f"{self.user.get_colaborando()}",color='black',pos_hint={'center_x':0.7,'center_y':0.82},size_hint=(.01,.01))
        self.perfil_user.insertWidget(colaborandoSize)

        nomePerfil = Label(text=self.user.get_nome(),color='black',pos_hint={'center_x':0.22,'center_y':0.74},size_hint=(.01,.01))
        self.perfil_user.insertWidget(nomePerfil)

        editar_btn = PersonalButton(self.editar_perfil,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',pos_hint={'center_x':0.5,'center_y':0.69},size_hint=(0.4,0.05),text="Editar Perfil",borderSize=1.5,borderColor=(0,0,0,1))
        self.perfil_user.insertWidget(editar_btn)

        linkedinLabel = Label(text=f"Linkedin: {self.user.get_linkedin()}",color='black',pos_hint={'center_x':0.5,'center_y':0.17},size_hint=(.01,.01))
        emailLabel = Label(text=f"Email: {self.user.get_email()}",color='black',pos_hint={'center_x':0.5,'center_y':0.14},size_hint=(.01,.01))
        githubLabel = Label(text=f"Web_site: {self.user.get_web_site()}",color='black',pos_hint={'center_x':0.5,'center_y':0.11},size_hint=(.01,.01))

        self.perfil_user.insertWidget(linkedinLabel)
        self.perfil_user.insertWidget(emailLabel)
        self.perfil_user.insertWidget(githubLabel)
        

        projetos = caixaRolagem(600,250,{"center_x":0.5,"center_y":0.46},spacing=0.2)
        self.perfil_user.insertWidget(projetos)

        my_posts = self.cliente.post_service.get_posts(self.user.get_id())
        for i,my_post in enumerate(my_posts):
            path = create_image_perfil(f"temp/post_{self.user.get_nome()}_{i}.png",my_post['image'])
            comentarios = len(self.cliente.post_service.get_comments(my_post['id']))
            project = Projeto(0.7,0.7,{"center_x":0.5,"center_y":0.8},path,my_post['curtir'],comentarios)
            project.show()
            projetos.add(project)

        self.rl.add_widget(self.perfil_user)
    
    def editar_perfil(self):
        self.rl.remove_widget(self.perfil_user)

        self.editarPerfil = Bloco(0.85,0.75,pos_hint={"center_x":0.5,"center_y":0.47})
        self.editarPerfil.setFormat("retangulo_arredondado",(1,1,1,1))

        btnVoltar = ImageButton(self.return_to_perfil,"Imagens/Voltar.png","circulo",pos_hint={'center_x':0.16,'center_y':0.88},size_hint=(0.05,0.05))
        self.editarPerfil.insertWidget(btnVoltar)

        self.carregar_img = BoxImage("circulo",self.user.get_path_image(),pos_hint={'center_x':0.22,'center_y':0.81},size_hint=(0.1,0.1))
        btnImage_perfil = PersonalButton(self.foto_perfil,(1,1,1,1),(0,0,0,1),15,"retangulo_arredondado",pos_hint={'center_x':0.22,'center_y':0.72},size_hint=(0.15,0.05),borderSize=1.5,borderColor=(0,0,0,1),text='Alterar imagem')
        
        self.editarPerfil.insertWidget(self.carregar_img)
        self.editarPerfil.insertWidget(btnImage_perfil)

        # Nome
        label_nome = Label(color='black',size_hint=(.2, .05),
                            pos_hint={'center_x': .38, 'center_y': .85}, text='Nome')
        
        self.nome = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),28,pos_hint={'center_x':.475,'center_y':.8},size_hint=(.25,.05),text=self.user.get_nome())
        self.editarPerfil.insertWidget(label_nome)
        self.editarPerfil.insertWidget(self.nome)
        #-----------------------------------------------------------------------------------------

        # Email
        label_email = Label(color='black',size_hint=(.2, .05),
                            pos_hint={'center_x': .38, 'center_y': .76}, text='E-mail')
        
        self.email = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),40,pos_hint={'center_x':.6,'center_y':.71},size_hint=(.5,.05),text=self.user.get_email())
        self.editarPerfil.insertWidget(label_email)
        self.editarPerfil.insertWidget(self.email)
        #----------------------------------------------------------------------------------------------------------------------

        # Aniversario
        label_aniversário = Label(color='black',size_hint=(.2, .05),
                            pos_hint={'center_x': .714, 'center_y': .85}, text='Data de nascimento')
        

        self.dia_aniversario = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),2,pos_hint={'center_x':.65,'center_y':.8},size_hint=(.04,.05),only_number=True,text=self.user.get_dia())
        
        label_barra = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .685, 'center_y': .8}, text='/',font_size=25)
        
        self.mes_aniversario = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),2,pos_hint={'center_x':.72,'center_y':.8},size_hint=(.04,.05),only_number=True,text=self.user.get_mes())

        label_barra2 = Label(color='black',size_hint=(.2, .05),
                            pos_hint={'center_x': .755, 'center_y': .8}, text='/',font_size=25)
        
        self.ano_aniversario = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),4,pos_hint={'center_x':.805,'center_y':.8},size_hint=(.07,.05),only_number=True,text=self.user.get_ano())

        self.editarPerfil.insertWidget(label_aniversário)
        self.editarPerfil.insertWidget(self.dia_aniversario)
        self.editarPerfil.insertWidget(label_barra)
        self.editarPerfil.insertWidget(self.mes_aniversario)
        self.editarPerfil.insertWidget(label_barra2)
        self.editarPerfil.insertWidget(self.ano_aniversario)
        #----------------------------------------------------------------------------------------------------------------------

        # Senha
        check_box = Interactive_Checkbox(self.exibirSenha,"Imagens/OlhoFechado.png",'Imagens/olhoAberto.png',pos_hint={'center_x':.746,'center_y':.62},size_hint=(.03,.025))
        label_senha = Label(text='Senha',color='black',pos_hint={'center_x':.377,'center_y':.67},size_hint=(.09,.05))
        self.senha = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,size_hint=(.37,.05),pos_hint={'center_x':.532,'center_y':.62},password=True,text=self.user.get_senha())
        self.editarPerfil.insertWidget(check_box)
        self.editarPerfil.insertWidget(label_senha)
        self.editarPerfil.insertWidget(self.senha)
        #----------------------------------------------------------------------------------------------------------------------

        # Separador
        separador = Geometry('retangulo',(0,0,0,0.2),pos_hint={'center_x':0.5,'center_y':0.57},size_hint=(.75,.003))
        self.editarPerfil.insertWidget(separador)
        #--------------------------------------------------------------------------------------

            
        label_estado = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .167, 'center_y': .54}, text='Estado')
        
        self.estado = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.232,'center_y':.5},size_hint=(.2,.05),text=self.user.get_estado())
        self.editarPerfil.insertWidget(label_estado)
        self.editarPerfil.insertWidget(self.estado)

        #________________________________


        # Cidade

        label_cidade = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .383, 'center_y': .54}, text='Cidade')
        
        self.cidade = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.473,'center_y':.5},size_hint=(.25,.05),text=self.user.get_cidade())
        self.editarPerfil.insertWidget(label_cidade)
        self.editarPerfil.insertWidget(self.cidade)

        #________________________________


        # Profissão

        label_profissao = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .66, 'center_y': .54}, text='Profissão')
        
        self.profissao = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.74,'center_y':.5},size_hint=(.25,.05),text=self.user.get_profissao())
        self.editarPerfil.insertWidget(label_profissao)
        self.editarPerfil.insertWidget(self.profissao)

        #________________________________


        # Universidade

        label_universidade = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .1875, 'center_y': .45}, text='Universidade')
        
        self.universidade = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.306,'center_y':.41},size_hint=(.35,.05),text=self.user.get_universidade())
        self.editarPerfil.insertWidget(label_universidade)
        self.editarPerfil.insertWidget(self.universidade)

        #________________________________


        # Curso

        label_curso = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .542, 'center_y': .45}, text='Curso')
        
        self.curso = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),25,pos_hint={'center_x':.69,'center_y':.41},size_hint=(.35,.05),text=self.user.get_curso())
        self.editarPerfil.insertWidget(label_curso)
        self.editarPerfil.insertWidget(self.curso)

        #________________________________

        
        # Web Site

        label_website = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .171, 'center_y': .36}, text='Web Site')
        
        self.website = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),100,pos_hint={'center_x':.5,'center_y':.315},size_hint=(.735,.05),text=self.user.get_web_site())
        self.editarPerfil.insertWidget(label_website)
        self.editarPerfil.insertWidget(self.website)

        #________________________________


        # Linkedin

        label_linkedin = Label(color='black',size_hint=(.2, .2),
                            pos_hint={'center_x': .171, 'center_y': .265}, text='Linkedin')
        
        self.linkedin = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),100,pos_hint={'center_x':.5,'center_y':.22},size_hint=(.735,.05),text=self.user.get_linkedin())
        self.editarPerfil.insertWidget(label_linkedin)
        self.editarPerfil.insertWidget(self.linkedin)

        #________________________________


        btnsalvar = PersonalButton(self.salvar_alteracao,(1,1,1,1),(0,0,0,1),15,"retangulo_arredondado",pos_hint={'center_x':0.5,'center_y':0.15},size_hint=(0.15,0.05),borderSize=1.5,borderColor=(0,0,0,1),text='Salvar')
        self.editarPerfil.insertWidget(btnsalvar)

        self.rl.add_widget(self.editarPerfil)

    def salvar_alteracao(self):
        if self.dir_img:
        # Salvar alteração das informações do usuário
            try:
                foto = imread(self.dir_img)
                self.user.set_new_path(self.dir_img)
                self.perfil_button.set_new_img(self.dir_img)
            except Exception:
                alerta = Alerta()
                alerta.start("Erro","Houve um erro ao ler a imagem!")
                foto = imread("Imagens/foto_perfil.jpg")
                self.user.set_new_path("Imagens/foto_perfil.jpg")
                self.perfil_button.set_new_img("Imagens/foto_perfil.jpg")
        
        else:
            foto = imread(self.user.get_path_image())

        atributos_necessarios = [self.email.get_text(),self.senha.get_text(),self.nome.get_text(),self.dia_aniversario.get_text(),self.mes_aniversario.get_text(),self.ano_aniversario.get_text()]
        erros = ["O campo de email é obrigatorio","O campo de senha é obrigatorio","O campo do nome é obrigatorio","O campo dia do aniversário é obrigatorio","O campo mes do aniversário é obrigatorio","O campo ano do aniversário é obrigatorio"]
        for i,atributo in enumerate(atributos_necessarios):
            if atributo == '':
                alerta = Alerta()
                alerta.start("Erro",erros[i])
                self.rl.add_widget(alerta)
        new_data = {
            "person":
            {
            "name":self.nome.get_text(),
            "birthday":f"{self.dia_aniversario.get_text()}/{self.mes_aniversario.get_text()}/{self.ano_aniversario.get_text()}",
            "email":self.email.get_text(),
            "password": self.senha.get_text(),
            "photo": serialize(foto).decode('latin1'),
            "state": self.estado.get_text(),
            "city": self.cidade.get_text()
            },
            "status":{
                "profession": self.profissao.get_text(),
                "university": self.universidade.get_text(),
                "course": self.curso.get_text(),
                "web_site": self.website.get_text(),
                "linkedin": self.linkedin.get_text()
            }
        }
        person = self.cliente.person_service.refresh_perfil(self.user.get_id(),new_data['person'])
        status = self.cliente.person_status_service.refresh_status(self.user.get_id(),new_data['status'])
        resposta = person and status
        if resposta == True:
            alerta = Alerta()
            alerta.start("Sucesso","Alterações efetuadas com sucesso!")
            self.rl.add_widget(alerta)
            self.user.set_nome(self.nome.get_text())
            self.user.set_profissao(self.profissao.get_text())
            self.user.set_cidade(self.cidade.get_text())
            self.user.set_estado(self.estado.get_text())
            self.user.set_curso(self.curso.get_text())
            self.user.set_data_nascimento(f"{self.dia_aniversario.get_text()}/{self.mes_aniversario.get_text()}/{self.ano_aniversario.get_text()}")
            self.user.set_email(self.email.get_text())
            self.user.set_universidade(self.universidade.get_text())
            self.user.set_web_site(self.website.get_text())
            self.user.set_senha(self.senha.get_text())
            self.user.set_linkedin(self.linkedin.get_text())
        else:
            alerta = Alerta()
            alerta.start("Erro","Houve um erro ao efetuar as altarações, favor verificar os campos novamente!")
            self.rl.add_widget(alerta)



    def exibirSenha(self,status):
        self.senha.password = not status
    
    def return_to_perfil(self):
        self.rl.remove_widget(self.editarPerfil)
        self.perfil()
    
    def foto_perfil(self):
        self.dir_img = Choose_file().get_dir()
        self.carregar_img.set_new_img(self.dir_img)

    def inserir_post_friends(self,id_post,curtidas,comentarios,text_post:Text,path_image_post:dict, nome:str, path_imagem_perfil:str):# Método chamado para inserir um post no feed do usuário
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
            foto_perfil = BoxImage('circulo',path_imagem_perfil,size_hint=(.1,.1),pos_hint={'center_x':0.22,'center_y':0.82})
            post.insertWidget(foto_perfil)

            arroba = Label(text=f'@{nome}',color='black',pos_hint={'center_x':0.4,'center_y':0.82},size_hint=(.01,.01))
            post.insertWidget(arroba)

            separador = Geometry('retangulo',(0,0,0,0.2),pos_hint={'center_x':0.5,'center_y':0.75},size_hint=(.8,.003))

            post.insertWidget(separador)

            text_post = Label(text=text_post,color='black',pos_hint={'center_x':0.5,'center_y':0.7},size_hint=(.01,.01))
            post.insertWidget(text_post)

            img_post = BoxImage('retangulo',path_image_post['path'],size_hint=(.6,.35),pos_hint={'center_x':0.5,'center_y':0.45})
            post.insertWidget(img_post)

            text_curtir = Label(text=str(curtidas),color='black',pos_hint={'center_x':0.32,'center_y':0.14},size_hint=(.01,.01))
            post.insertWidget(text_curtir)

            curtir_button = PersonalButton(self.post_curtido,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',argsAction=[id_post,text_curtir],pos_hint={'center_x':0.32,'center_y':0.2},size_hint=(0.3,0.05),text="Curtir",borderSize=1.5,borderColor=(0,0,0,1))
            post.insertWidget(curtir_button)

            text_comentar = Label(text=f"{comentarios}",color='black',pos_hint={'center_x':0.68,'center_y':0.14},size_hint=(.01,.01))
            post.insertWidget(text_comentar)

            comentar_button = PersonalButton(self.comentar_post,(1,1,1,1),(0,0,0,1),12,'retangulo_arredondado',argsAction=[post,id_post,text_comentar],pos_hint={'center_x':0.68,'center_y':0.2},size_hint=(0.3,0.05),text="Comentar",borderSize=1.5,borderColor=(0,0,0,1))
            post.insertWidget(comentar_button)

            post.freeze_state()

            self.feed.add(post)

    def inserir_post(self,text_post:Text,path_image_post:dict):
        do = True
        if self.postagem:
            try:
                path_image_post['path']
                self.restore_to_feed()
                self.postagem = None
            except Exception:
                do = False
        if do:
            try:
                imagem = imread(path_image_post['path'])
            except Exception:
                alerta = Alerta()
                alerta.start("Erro","A imagem enviada não é válida")
                self.rl.add_widget(alerta)
                imagem = None

            
            data_post = {"text":text_post.text,
                        "image":serialize(imagem).decode('latin1'),
                        "curtir": 0,
                        "date": datetime.datetime.now(),
                        "author_id": self.user.get_id()}
            
            postado = self.cliente.post_service.create_post(data_post)
            if postado:
                alerta = Alerta()
                alerta.start("Sucesso","Post criado com sucesso !")
            else:
                alerta = Alerta()
                alerta.start("Erro","Erro ao tentar inserir post!")
            
            self.rl.add_widget(alerta)

    def post_curtido(self,id_post,text_curtidas:Label):
        text_curtidas.text = str(int(text_curtidas.text) + 1)
        self.cliente.post_service.curtir_post(id_post)

    def comentar_post(self,post:Post,id_post,text_comentar): # Tem que receber as informações do post (quem enviou o post e os comentarios existentes)
        post.clearWidgets()
        comentario_post = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),35,pos_hint={"center_x":0.47,'center_y':0.2},size_hint=(.6,.07))
        btn_send = ImageButton(self.enviar_comentario_post,"Imagens/btn_send2.png","retangulo",argsAction=[post,comentario_post,id_post,text_comentar],size_hint=(.06,.05),pos_hint={"center_x":0.82,'center_y':0.2})
        post.insertWidget(btn_send)
        post.insertWidget(comentario_post)
        btnVoltar = ImageButton(post.go_to_freeze_state,"Imagens/Voltar.png","circulo",pos_hint={'center_x':0.15,'center_y':0.82},size_hint=(0.05,0.05))
        post.insertWidget(btnVoltar)
        
        comentarios = self.cliente.post_service.get_comments(id_post)
        for comentario in comentarios:
            texto = comentario['text']
            foto = self.cliente.person_service.get_person(comentario['author_id'])['photo'] # Ainda n ta funcionando (acho que o erro está no author_id)
            path_perfil = create_image_perfil(f"temp/post_perfil_comentario{comentario['author_id']}.png",foto)
            foto_perfil = BoxImage('circulo',path_perfil,size_hint=(.05,.05),pos_hint={'center_x':0.22,'center_y':0.82})
            comentLabel = Label(text=f'{texto}',color='black',pos_hint={'center_x':0.5,'center_y':0.82},size_hint=(.01,.01))
            post.comment(foto_perfil,comentLabel)
    
    def enviar_comentario_post(self,post:Post,comentario:Text,id_post,text_comentar:Text):# Tem que receber as informações do post para poder enviar o comentario, assim como quem fez o comentario
        if len(comentario.get_text()) > 0:
            text_comentar.text = str(int(text_comentar.text)+1)
            resposta = self.cliente.comment_service.insert_comment(id_post,self.user.get_id(),comentario.get_text())
            if resposta:
                foto_perfil = BoxImage('circulo',self.user.get_path_image(),size_hint=(.05,.05),pos_hint={'center_x':0.22,'center_y':0.82})
                comentLabel = Label(text=f'{comentario.get_text()}',color='black',pos_hint={'center_x':0.5,'center_y':0.82},size_hint=(.01,.01))
                post.comment(foto_perfil,comentLabel)