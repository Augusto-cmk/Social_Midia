from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from Visao.Recursos.Botao import PersonalButton
from kivy.uix.label import Label

class Alerta(RelativeLayout):
    def __init__(self,**args):
        super().__init__(**args)
        box = RelativeLayout()
        ok = PersonalButton(self.action,(1,1,1,1),(0,0,0,1),15,'circulo',pos_hint={'center_x':0.9,'center_y':0.12},size_hint=(.09,.2),text='Ok')
        self.msg = Label(pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(.09,.05),color='white')
        box.add_widget(self.msg)
        box.add_widget(ok)
        self.pop = Popup(size_hint=(.5,.3),pos_hint={'center_x':0.5,'center_y':0.5},content=box)
    
    def start(self,title,mensagem):
        self.pop.title = title
        self.msg.text = mensagem
        self.add_widget(self.pop)

    def action(self):
        self.remove_widget(self.pop)


