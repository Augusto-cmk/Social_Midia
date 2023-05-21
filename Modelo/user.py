from Comunication.mensagem import deserialize
from cv2 import imwrite
class User:
    def __init__(self) -> None:
        self.id = None
        self.foto = None
        self.nome = None
        self.dia = None
        self.mes = None
        self.ano = None
        self.email = None
        self.senha = None
        self.cidade = None
        self.estado = None
        self.universidade = None
        self.curso = None
        self.profissao = None
        self.web_site = None
        self.linkedin = None
        self.colaboradores = None
        self.colaborando = None
        
    def get_id(self):
        return self.id
    
    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def set_data_nascimento(self, data:str):
        self.dia = data[0:2]
        self.mes = data[3:5]
        self.ano = data[6:]
    
    def get_dia(self):
        return self.dia
    
    def get_mes(self):
        return self.mes

    def get_ano(self):
        return self.ano
    
    def set_email(self, email):
        self.email = email
    
    def get_email(self):
        return self.email
    
    def set_senha(self,senha):
        self.senha = senha

    def get_senha(self):
        return self.senha
    
    def set_cidade(self, cidade):
        self.cidade = cidade

    def get_cidade(self):
        return self.cidade

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado
    
    def set_universidade(self, universidade):
        self.universidade = universidade

    def get_universidade(self):
        return self.universidade

    def set_curso(self, curso):
        self.curso = curso
    
    def get_curso(self):
        return self.curso

    def set_profissao(self, profissao):
        self.profissao = profissao

    def get_profissao(self):
        return self.profissao

    def set_web_site(self,web_site):
        self.web_site =  web_site

    def get_web_site(self):
        return self.web_site

    def set_linkedin(self, linkedin):
        self.linkedin = linkedin
    
    def get_linkedin(self):
        return self.linkedin

    def set_colaboradores(self, colaboradores):
        self.colaboradores = colaboradores
    
    def get_colaboradores(self):
        return self.colaboradores
    
    def set_colaborando(self, colaborando):
        self.colaborando = colaborando
    
    def get_colaborando(self):
        return self.colaborando

    def set_image_perfil(self,image_bd:str):
        image_bytes = bytes(image_bd)
        image = deserialize(image_bytes)
        self.foto = "temp/img_perfil_user.png"
        imwrite(self.foto,image)
    
    def get_path_image(self):
        return self.foto
        
                