from kivy.graphics import Ellipse, Color,RoundedRectangle,Rectangle,Line
from kivy.uix.widget import Widget


class Geometry(Widget):
    def __init__(self,format,color,borderSize=0,borderColor=(1,1,1,1),**kwargs):
        super().__init__(**kwargs)

        forms = {"circulo":Ellipse(),"retangulo":Rectangle(),"retangulo_arredondado":RoundedRectangle()}
        self.format = format
        self.color = Color(*color)
        self.shape = forms[format]

        self.borderColor = Color(*borderColor)
        self.borderSize = borderSize

        self.borda = Line()
        

        if self.borderSize > 0:
            self.canvas.add(self.borderColor)
            self.canvas.add(self.borda)

        self.canvas.add(self.color)
        self.canvas.add(self.shape)
    
    def on_size(self, *args):
        self.shape.size = self.size
        self.shape.pos = self.pos
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


