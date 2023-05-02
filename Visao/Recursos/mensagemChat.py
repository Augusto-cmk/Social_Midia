from kivy.graphics import Ellipse, Color,RoundedRectangle,Rectangle,Line
from kivy.uix.label import Label

class Mensagem(Label):
    """
        Essa classe é uma implementação de um widget de mensagem em uma interface gráfica de usuário (GUI) em Python, utilizando o framework Kivy.

        A classe herda da classe Widget do Kivy e tem um construtor que recebe os seguintes parâmetros:

        - text: o texto da mensagem
        - textSize: o tamanho da fonte do texto
        - sended: um valor booleano que indica se a mensagem foi enviada ou recebida
        - font_text: a fonte do texto (o padrão é "Roboto")
        - borderSize: o tamanho da borda da mensagem (o padrão é 0)
        - borderColor: a cor da borda da mensagem (o padrão é branco)
        - **kwargs: outros argumentos opcionais que podem ser passados.
        
        * O método init é responsável por inicializar os atributos da classe, definir a posição e a cor da mensagem (de acordo com o parâmetro sended), definir a forma da mensagem (de acordo com o parâmetro format), adicionar um widget de texto com o conteúdo da mensagem e desenhar a mensagem na tela.

        * O método on_size é responsável por ajustar o tamanho da mensagem e do widget de texto quando a mensagem é redimensionada.

        * O método on_pos é responsável por ajustar a posição e o desenho da borda da mensagem quando a mensagem é movida.

        * O método __setBarraN é uma função auxiliar que quebra o texto da mensagem em várias linhas, adicionando caracteres de quebra de linha (\n) quando a largura do texto excede um valor máximo definido (43 por padrão).

        Em resumo, essa classe é uma implementação de um widget de mensagem personalizável que pode ser usado em uma GUI desenvolvida com o Kivy.
    """
    def __init__(self,text,textSize,sended,font_text="Roboto",**kwargs):
        super().__init__(**kwargs)
        self.font_size = textSize
        self.font_name = font_text
        self.background_color = [0, 0, 0, 0]
        self.color='black'
        self.pos[0] = 300 - 300*(len(text) - 1)/100
        if not sended:
            self.color='red'
            self.pos[0] = 300*(len(text) - 1)/100


        # adicionar widget de texto
        self.text = text