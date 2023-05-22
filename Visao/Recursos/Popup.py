from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Botao import PersonalButton
from Visao.Recursos.Text import Text
from kivy.uix.label import Label

class Alerta(RelativeLayout):
    def __init__(self,**args):
        super().__init__(**args)
        box = RelativeLayout()
        ok = PersonalButton(self.action,(1,1,1,1),(0,0,0,1),15,'circulo',pos_hint={'center_x':0.9,'center_y':0.12},size_hint=(.09,.2),text='Ok')
        self.msg = Label(pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(.09,.05),color='white')
        box.add_widget(self.msg)
        box.add_widget(ok)
        self.pop = Popup(size_hint=(.7,.3),pos_hint={'center_x':0.5,'center_y':0.5},content=box)
        self.aberto = False
    
    def start(self,title,mensagem):
        self.pop.title = title
        self.msg.text = mensagem
        self.add_widget(self.pop)
        self.aberto = True

    def action(self):
        self.remove_widget(self.pop)
        self.aberto = False
    
    def is_open(self):
        return self.aberto
    


class Confirmar_Email(RelativeLayout):
    def __init__(self,**args):
        super().__init__(**args)
        box = RelativeLayout()
        ok = PersonalButton(self.action,(1,1,1,1),(0,0,0,1),15,'circulo',pos_hint={'center_x':0.9,'center_y':0.12},size_hint=(.09,.2),text='Ok')
        confirmar = PersonalButton(self.confirm,(1,1,1,1),(0,0,0,1),15,'circulo',pos_hint={'center_x':0.7,'center_y':0.12},size_hint=(.2,.2),text='Confirmar')
        self.msg = Label(pos_hint={'center_x':0.5,'center_y':0.8},size_hint=(.09,.05),color='white')
        self.codigo = Text((1,1,1,1),(0,0,0,1),15,(0,0,0,1),10,only_number=True,pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(.3,.25))
        self.number = None
        box.add_widget(self.msg)
        box.add_widget(self.codigo)
        box.add_widget(confirmar)
        box.add_widget(ok)
        self.pop = Popup(size_hint=(.7,.3),pos_hint={'center_x':0.5,'center_y':0.5},content=box)
    
    def start(self,codigo):
        self.pop.title = 'Confirmação de e-mail'
        self.msg.text = "Favor inserir o código enviado no seu e-mail cadastrado"
        self.number = str(codigo)
        self.add_widget(self.pop)

    def action(self):
        self.remove_widget(self.pop)
    
    def confirm(self):
        if self.codigo.get_text() == self.number:
            self.remove_widget(self.pop)
        else:
            self.msg.text = 'Código incorreto, favor tentar novamente!'



