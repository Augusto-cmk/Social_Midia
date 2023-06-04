from Comunication.mensagem import deserialize
from cv2 import imwrite
from unidecode import unidecode
from random import randint
import os
class User:
    def __init__(self) -> None:
        self.id = ''
        self.foto = ''
        self.nome = ''
        self.dia = ''
        self.mes = ''
        self.ano = ''
        self.email = ''
        self.senha = ''
        self.cidade = ''
        self.estado = ''
        self.universidade = ''
        self.curso = ''
        self.profissao = ''
        self.web_site = ''
        self.linkedin = ''
        self.colaboradores = ''
        self.colaborando = ''

    def set_id(self,id):
        self.id = id
        
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
    
    def set_new_path(self,path):
        self.foto = path

    def set_image_perfil(self,image_bd:str):
        path = f"temp/img_perfil_user{self.nome}_{randint(1,1000)}.png"
        self.foto = create_image_perfil(path,image_bd)
    
    def get_path_image(self):
        return self.foto
        

def create_image_perfil(path,image_bd:str)->str:
    image_bytes = image_bd.encode('latin1')
    image = deserialize(image_bytes)
    new_path = unidecode(path)
    imwrite(new_path,image)
    return new_path