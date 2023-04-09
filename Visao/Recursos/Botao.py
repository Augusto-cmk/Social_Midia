from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Ellipse, Color,RoundedRectangle,Rectangle,Line
from kivy.animation import Animation
from kivy.uix.widget import Widget

# Fazer com que a cor do círculo seja personalizavel na classe
# Fazer com que a cor do texto seja personalizavel na classe

class PersonalButton(Button):
    """
    Ao instanciar a classe PersonalButton, é preciso passar a função "action" como parâmetro. Esse método,
    é responsável por realizar a ação quando o botão é acionado.

     - colorButton = Cor a ser definida para o botao
     - colorText = Cor a ser definida para o texto
     - textSize = Tamanho da fonte do texto
     - font_text = Fonte do texto (Por padrão ela ja vem com a fonte Roboto)
    
    Esta possui as seguintes opções:
        - Roboto
        - Incluir uma fonte personalisada, passando um arquivo .ttf (font_text = minha_fonte.ttf)
    
    Segue um exemplo de uso da classe:
         Button = PersonalButton(action=self.acao,size_hint=(.09, .05),
                        pos_hint={'center_x': .5, 'center_y': .5},
                        text="Teste",colorButton=(1,1,1,1),colorText=(0,0,0,1),textSize=15,format='retangulo_arredondado',borderColor=(1,0,1,1),borderSize=2)
        
         - O parâmetro pos_hint é herdado da classe Button do kivy, e nele são passadas as coodenadas x e y
            onde o botão vai ficar na tela caso esteja utilizando um RelativeLayout

         - O parâmetro size_hint também é herdado da classe Button, sendo ele a definição do tamanho do botão

         - O parâmetro format possui as seguintes alternativas:
            - 'circulo' (Para efetivamente ser um circulo o size_hint deve ter o mesmo tamanho em altura e largura)
            - 'retangulo' (Para ser um quadrado o size_hint deve ter o mesmo tamanho em altura e largura)
            - 'retangulo_arredondado'
        
        - O parâmetro borderSize refere-se a largura da borda a ser desenhada. Por padrão ela vem 0, ou seja, não desenha nenhuma borda
        - O parâmetro borderColor refere-se a cor da borda a ser desenhada. Por padrão ela vem com a cor preta.
        
    
    O esquema de cores da classe possui os seguintes parâmetros (red, green, blue, alpha)

    """
    def __init__(self,action,colorButton,colorText,textSize,format,font_text="Roboto",borderSize=0,borderColor=(1,1,1,1),**kwargs):
        super(PersonalButton, self).__init__(**kwargs)
        self.defaultSize = self.size_hint.copy()
        self.action = action
        self.borderSize = borderSize
        # definir cor e tamanho do texto do botão
        self.color = colorText
        self.font_size = textSize
        self.font_name = font_text
        self.background_color = [0, 0, 0, 0]
        
        # definir cor do círculo
        self.shape_color = Color(*colorButton)
        self.border_color = Color(*borderColor)
        
        self.format = format

        self.borda = Line()
        # desenhar figura
        if format == 'circulo':
            self.shape = Ellipse()
        
        if format == 'retangulo':
            self.shape = Rectangle()
        
        if format == 'retangulo_arredondado':
            self.shape = RoundedRectangle()

        if self.borderSize > 0:
            self.canvas.add(self.border_color)
            self.canvas.add(self.borda)

        self.canvas.add(self.shape_color)
        self.canvas.add(self.shape)

        # adicionar widget de texto
        self.label = Label(text=self.text, color=self.color, font_size=self.font_size, font_name=self.font_name,
                            pos_hint=self.pos_hint, halign='center', valign='middle')

        self.add_widget(self.label)

    def on_size(self, *args):
        self.shape.size = self.size
        self.shape.pos = self.pos
        self.label.size = self.size
        if self.borderSize > 0:
            self.borda.width=self.borderSize

    def on_pos(self, *args):
        if self.borderSize > 0:
            if self.format == 'circulo':
                self.borda.ellipse=(self.x, self.y, self.width, self.height)

            if self.format == 'retangulo':
                self.borda.rectangle=(self.x, self.y, self.width, self.height)
            
            if self.format == 'retangulo_arredondado':
                self.borda.rounded_rectangle=(self.pos[0],self.pos[1],self.size[0],self.size[1],10,10,10,10)

        self.shape.pos = self.pos
        self.label.pos = self.pos
    
    def on_press(self):
        self.action()
        anim_size_hint = Animation(size_hint=[self.defaultSize[0]+0.02,self.defaultSize[1]+0.02], duration=0.1) + Animation(size_hint=[self.defaultSize[0]+0.01,self.defaultSize[1]+0.01], duration=0.1)
        
        anim_size_hint.start(self)

        anim_size_hint.bind(on_complete=self.restore_size_hint)
    
    def restore_size_hint(self, *args):
        self.size_hint = self.defaultSize.copy()

class ImageButton(Button):
    def __init__(self,**kw):
        super().__init__(**kw)