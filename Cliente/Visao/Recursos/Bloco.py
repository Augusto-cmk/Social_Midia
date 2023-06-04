from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from Visao.Recursos.Geometry import Geometry
from kivy.graphics import Ellipse, Color,RoundedRectangle,Rectangle
from kivy.uix.label import Label


class Bloco(RelativeLayout):
    """
        Esta classe tem como finalidade de criar um bloco na tela, onde os recursos fiquem armazenados 
        em uma forma geométrica, de maneira a organizar os dados.

        A classe possui os seguintes parâmetros:
            - altura = altura da forma do bloco
            - largura = largura da forma do bloco
            - pos_hint = posição na tela
                - Usa-se da serguinte forma:
                    - {'center_x':valor,'center_y':valor} 
        
        Exemplo de uso da classe:
            -   bloco = Bloco(.5,.5,{'center_x': .4, 'center_y': .6})
                bloco.setFormat("retangulo_arredondado",(1,0,0,1))

                Button = PersonalButton(action=self.acao,size_hint=(.09, .05),
                                pos_hint={'center_x': .3, 'center_y': .5},
                                text="Teste",colorButton=(1,1,1,1),colorText=(0,0,0,1),textSize=15,format='retangulo_arredondado',borderColor=(1,0,1,1),borderSize=2)

                bloco.insertWidget(Button)
    """
    def __init__(self,altura,largura,pos_hint,**kw):
        super().__init__(**kw)

        self.pos_hint = pos_hint
        self.height = altura
        self.width = largura
        self.widgets = list()
    
    def freeze_state(self):
        self.freezed_state = self.widgets.copy()
    
    def go_to_freeze_state(self):
        self.clearWidgets()
        for widget in self.freezed_state: 
            self.add_widget(widget)
            self.widgets.append(widget)
    
    def setFormat(self,format,color,borderSize=0,borderColor=(1,1,1,1)):
        """
        Esse método é um método necessário na classe, pois vai definir a forma do bloco,
        permitindo que configure a cor, forma e a sua borda

        Os parâmetros do método são:
            - format = formato da forma física (circulo, retangulo, retangulo_arredondado)
            - color = cor do bloco (Passa-se uma tupla com os valores de (red, green, blue, alpha))
            - borderSize = espessura da borda (caso queira) por padrão o tamanho é 0, ou seja, sem borda.
            - borderColor = cor da borda a ser inserida. Funciona da mesma forma que a cor do bloco. 
              Por padrão ela vem branca
        """
        self.format = format
        self.color = color
        self.borderSize = borderSize
        self.borderColor = borderColor
        self.add_widget(Geometry(format,color,borderSize,borderColor,size_hint=(self.width,self.height),pos_hint=self.pos_hint))
    
    def insertWidget(self,widget:Widget):
        """
            Só é recomendado utilizar esse método quando já foi setado a forma do bloco!
            Este método tem como finalidade a inserção de widgets no bloco, sendo necessário passar a posição do mesmo
        """
        pos_hint_widget = widget.pos_hint.copy()
        center = self.pos_hint.copy()

        widget.pos_hint = self.__alinhar(center,pos_hint_widget)

        self.add_widget(widget)
        self.widgets.append(widget)
    
    def removeWidget(self,widget:Widget):
        self.remove_widget(widget)
        self.widgets.remove(widget)
    
    def clearWidgets(self):
        for widget in self.widgets:
            self.remove_widget(widget)
        
        self.widgets = list()

    def reajuste(self):
        center = self.pos_hint.copy()
        for widget in self.widgets:
            natural_center_y = 0.5
            center_y = center['center_y']
            dif_y = natural_center_y - center_y
            result = mod(widget.pos_hint['center_y'] - dif_y - 0.29)
            widget.pos_hint['center_y'] = result

    def __alinhar(self,centro,pos_hint_widget)->dict:
        """
            Vai determinar a posição realocada do widget, determinando a posição correta dentro do bloco
        """
        natural_center_x = 0.5
        natural_center_y = 0.5

        center_x = centro['center_x']
        center_y = centro['center_y']

        
        dif_x = natural_center_x - center_x
        dif_y = natural_center_y - center_y
        return {'center_x':pos_hint_widget['center_x']-dif_x,'center_y':pos_hint_widget['center_y']-dif_y}
    
class Post(Bloco):
    def __init__(self, altura, largura, pos_hint, **kw):
        super().__init__(altura, largura, pos_hint, **kw)
        self.i = 0
        self.comentarios = list()
    
    def comment(self,BoxImagePerfil,LabelComentario):
        if len(self.comentarios) < 6:
            # Ajuste de altura
            BoxImagePerfil.pos_hint['center_y'] -= self.i
            LabelComentario.pos_hint['center_y'] -= self.i
            # -----------------------------------------
            self.comentarios.append((BoxImagePerfil,LabelComentario))
            self.insertWidget(BoxImagePerfil)
            self.insertWidget(LabelComentario)
            self.i += 0.1
    
    def reset_comments(self):
        for comentario in self.comentarios:
            self.removeWidget(comentario[0])
            self.removeWidget(comentario[1])
        self.i = 0
        self.comentarios = list()
    
    def go_to_freeze_state(self):
        self.reset_comments()
        return super().go_to_freeze_state()

class Projeto(Bloco):
    def __init__(self, altura, largura, pos_hint,image_project,sizelikes,sizefeedbacks, **kw):
        super().__init__(altura, largura, pos_hint, **kw)
        self.image_project = image_project
        self.sizelikes = sizelikes
        self.sizefeedbacks = sizefeedbacks
    
    def show(self):
        self.setFormat("retangulo_arredondado",(1,1,1,1),borderSize=5,borderColor=(0,0,0,1))
        image = BoxImage("retangulo",self.image_project,size_hint=(.4,.4),pos_hint={'center_x':0.5,'center_y':0.6})

        like = BoxImage("retangulo","Imagens/like_image.png",size_hint=(.2,.2),pos_hint={'center_x':0.25,'center_y':0.25})
        labelLike = Label(text=f"{self.sizelikes}",color='black',pos_hint={'center_x':0.25,'center_y':0.17},size_hint=(.01,.01))
        self.insertWidget(like)
        self.insertWidget(labelLike)

        feedback = BoxImage("retangulo","Imagens/comentario.png",size_hint=(.2,.2),pos_hint={'center_x':0.75,'center_y':0.25})
        labelFeedback = Label(text=f"{self.sizefeedbacks}",color='black',pos_hint={'center_x':0.75,'center_y':0.17},size_hint=(.01,.01))
        self.insertWidget(feedback)
        self.insertWidget(labelFeedback)

        self.insertWidget(image)
        

class BoxImage(Widget):
    """
        A classe BoxImage tem como foco, criar um box para inserir a imagem do formato que deseja

        - size_hint = tamanho da figura
        - format = formato da figura (circulo, retangulo,retangulo_arredondado)
        - pos_hint = posição da figura na tela
        - pathImage = caminho da imagem

        Segue um exemplo de uso da classe:
            image = BoxImage("circulo","Imagens/mais.png",size_hint=(.09, .05),
                            pos_hint={'center_x': .5, 'center_y': .5})
    """
    def __init__(self,format,pathImage, **kw):
        super().__init__(**kw)
        self.background_color = [0, 0, 0, 0]
        self.format = format
        if format == 'circulo':
            self.shape = Ellipse(source=pathImage)
        if format == 'retangulo':
            self.shape = Rectangle(source=pathImage)
        if format == 'retangulo_arredondado':
            self.shape = RoundedRectangle(source=pathImage)
        
        self.canvas.add(Color((1,1,1,1)))
        self.canvas.add(self.shape)

    def set_new_img(self,pathImage):
        if len(pathImage) > 0:
            self.canvas.remove(self.shape)
            if self.format == 'circulo':
                self.shape = Ellipse(source=pathImage)
            if self.format == 'retangulo':
                self.shape = Rectangle(source=pathImage)
            if self.format == 'retangulo_arredondado':
                self.shape = RoundedRectangle(source=pathImage)
            
            self.canvas.add(Color((1,1,1,1)))
            self.canvas.add(self.shape)
            self.on_size()
            self.on_pos()

    def on_size(self, *args):
        self.shape.size = self.size

    def on_pos(self, *args):
        self.shape.pos = self.pos


def mod(value):
    return value if value >0 else value*(-1)