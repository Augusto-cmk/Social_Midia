from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color,RoundedRectangle,Rectangle,Line
from kivy.uix.label import Label

class Mensagem(Widget):
    def __init__(self,text,textSize,format,sended,font_text="Roboto",borderSize=0,borderColor=(1,1,1,1),**kwargs):
        super().__init__(**kwargs)
        self.borderSize = borderSize
        self.font_size = textSize
        self.font_name = font_text
        self.background_color = [0, 0, 0, 0]

        tam = len(text) if len(text) <= 43 else 43
        newtext = self.__setBarraN(text)
        barrasN = newtext.count('\n')

        self.size_hint[1] += barrasN/100
        self.size_hint[0] += tam/100
        if sended:
            self.pos_hint = {'center_x':0.7,'center_y':0.7}
            self.pos_hint['center_x'] -= (0.004762)*(tam-1)
            colorMSG = (1,1,1,1)
            self.color = (0,0,0,1)
        else:
            self.pos_hint = {'center_x':0.3,'center_y':0.7} 
            self.pos_hint['center_x'] += (0.004762)*(tam-1)
            colorMSG = (0,0,0,1)
            self.color = (1,1,1,1)


        print(newtext)
        # definir cor do círculo
        self.shape_color = Color(*colorMSG)
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
        self.label = Label(text=newtext, color=self.color, font_size=self.font_size, font_name=self.font_name,
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
    
    def __setBarraN(self,text:str,max_length=43):
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= max_length:
                if current_line:
                    current_line += " "
                current_line += word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return "\n".join(lines)