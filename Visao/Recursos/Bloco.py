from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from Visao.Recursos.Geometry import Geometry

class Bloco(Screen):
    """
        Esta classe tem como finalidade de criar um bloco na tela, onde os recursos fiquem armazenados 
        em uma forma geométrica, de maneira a organizar os dados.

        A classe possui os seguintes parâmetros:
            - altura = altura da forma do bloco
            - largura = largura da forma do bloco
            - pos_hint = posição na tela
                - Usa-se da serguinte forma:
                    - {'center_x':valor,'center_y':valor} 
        
    """
    def __init__(self,altura,largura,pos_hint,**kw):
        super().__init__(**kw)

        self.rl = RelativeLayout()
        self.rl.pos_hint = pos_hint
        self.rl.height = altura
        self.rl.width = largura


        self.add_widget(self.rl)
    
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
        self.rl.add_widget(Geometry(format,color,borderSize,borderColor,size_hint=(self.rl.width,self.rl.height),pos_hint=self.rl.pos_hint))
    
    def insertWidget(self,widget:Widget):
        """
            Só é recomendado utilizar esse método quando já foi setado a forma do bloco!
            Este método tem como finalidade a inserção de widgets no bloco, sendo necessário passar a posição do mesmo
        """
        pos_hint_widget = widget.pos_hint.copy()
        center = self.rl.pos_hint.copy()

        widget.pos_hint = self.__alinhar(center,pos_hint_widget)
        
        self.rl.add_widget(widget)
    
    def removeWidget(self,widget:Widget):
        self.rl.remove_widget(widget)
    
    def clearWidgets(self):
        self.rl.clear_widgets


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