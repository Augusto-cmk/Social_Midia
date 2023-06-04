from kivy.uix.button import Button
from kivy.graphics import Ellipse,RoundedRectangle,Rectangle


class Interactive_Checkbox(Button):
    """
        Esta classe tem como propósito definir duas imagen para quando o botão foi pressionado e quando não foi pressionado
        Isso vai dar a sensação de que o botão vai ter interação com o usuário
    """
    def __init__(self,action,not_allow_image,allow_image,**kwargs):
        super().__init__(**kwargs)
        self.action = action
        self.background_color = [0, 0, 0, 0]
        self.shape = Rectangle(source=not_allow_image)
        self.canvas.add(self.shape)
        self.images = {True:allow_image,False:not_allow_image}
        self.status = False

    def on_size(self, *args):
        self.shape.size = self.size

    def on_pos(self, *args):
        self.shape.pos = self.pos
    
    def on_press(self):
        self.status = not self.status
        self.shape.source = self.images[self.status]
        self.action(self.status)
        return super().on_press()