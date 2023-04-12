from kivy.uix.textinput import TextInput

class Text(TextInput):
    """
        - colorBox= Cor a ser definida para a caixa de texto
        - colorText = Cor a ser definida para o texto
        - textSize = Tamanho da fonte do texto
        - font_text = Fonte do texto (Por padrão ela ja vem com a fonte Roboto)
        - only_number = Se devem ser aceitos apenas números (Por padrão = False)
        - max_caracter = Quantidade máxima de caracteres permitidos
        - cursorColor = Cor do cursor da caixa de texto

        OBS: Não esquecer de definir a posição da caixa na tela, bem como o seu tamanho e largura.

        Exemplo de uso da classe:

        txt = Text((1,1,1,1),(1,0,0,1),15,(0,0,0,1),pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.2,0.05),max_caracter=10,only_number=True)
    """
    def __init__(self,colorBox,colorText,textSize,cursorColor,max_caracter,only_number=False,font_text="Roboto",**kwargs):
        super().__init__(**kwargs)
        self.background_color = [*colorBox]
        self.color = colorText
        self.font_size = textSize
        self.font_name = font_text
        self.cursor_color = [*cursorColor]
        self.max_caracter = max_caracter
        self.only_number = only_number

    def get_text(self):
        return self.text

    def keyboard_on_textinput(self, window, text):
        if len(self.text) < self.max_caracter and self.__is_number(text):
            return super().keyboard_on_textinput(window, text)


    def __is_number(self,caracter):
        if self.only_number:
            try:
                int(caracter)
                return True
            except Exception:
                return False
        return True