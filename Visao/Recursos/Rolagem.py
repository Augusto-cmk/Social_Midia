from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

class caixaRolagem(RelativeLayout):
    """
        Para que os widgets sejam funcionais na classe, os mesmos devem ter o método "reajuste", que fará o reajuste das posições dos widgets
        Isso é necessário, quando o widget possui outros widgets inseridos no mesmo

        O parâmetro que o reajuste recebe é o spacing, que é o valor de espaçamento entre os widgets dessa classe. Esse valor vai determinar
        qual o valor de reajuste necessário para obter a posição correta do widget. Vale resaltar que o mesmo realiza o reajuste apenas no eixo y

        Caso tenha dúvida de como funciona o método de reajuste, consulte o método de reajuste da classe Bloco

        Esta classe permite que seja adicionado uma caixa para rolar os widgets adicionados.
        Para a configuração da mesma, é necessário entender os parâmetros.
        Os parâmetros que a classe usa são os seguintes:
            - listaWidgets = Lista de widgets que serão adicionados na caixa (Precisa ser uma lista, mesmo sendo apenas 1 elemento)
            - cols = número de colunas que serão inseridas no layout de rolagem
                - Se forem duas colunas por exemplo, o layout vai organizar os widgets par a par
            - spacing = espaçamento entre os widgets
            - row_default_height = altura que cada widget pode ter dentro da caixa 
            - padding = preenchimento do widget na caixa
            - col_default_width = Largura padrão para os widgets

        - Os valores descritos, vem com valores padrão, mas que podem ser personalizados caso necessário

        Exemplo de uso da classe:

            -   bloco = Bloco(.5,.5,{'center_x': .4, 'center_y': .6})
                bloco.setFormat("retangulo_arredondado",(1,0,0,1))

                Button = PersonalButton(action=self.acao,size_hint=(.09, .05),
                                pos_hint={'center_x': .3, 'center_y': .5},
                                text="Teste",colorButton=(1,1,1,1),colorText=(0,0,0,1),textSize=15,format='retangulo_arredondado',borderColor=(1,0,1,1),borderSize=2)

                bloco.insertWidget(Button)

                rolagem = caixaRolagem()

                rolagem.add(bloco)

        OBS: Somente os widgets que forem adicionados a essa caixa de rolagem, vão ter a capacidade de serem listados e movidos pela barra.
        Caso insira essa caixa de rolagem em um outro layout com widgets fixos, os mesmos não irão se mover
    """
    def __init__(self, width, height,pos_hint,cols=1,spacing=0.4,row_default_height=500,padding=100,col_default_width=100,**kwargs):
        super().__init__(**kwargs)


        self.width = width
        self.height = height
        self.pos_hint = pos_hint
        scroll = ScrollView(size_hint=(None, None), size=(width, height),pos_hint=pos_hint)
        self.spacing = spacing

        self.layout = GridLayout(cols=cols,size_hint_y=None,row_force_default=True,row_default_height=row_default_height,col_default_width=col_default_width,padding=padding)
        self.layout.bind(minimum_height = self.layout.setter('height'))

        self.i = 0

        scroll.bar_width = 10
        scroll.add_widget(self.layout)
        self.add_widget(scroll)

    def add(self,widget):
        if self.i > 0:
            widget.pos_hint['center_y'] += self.spacing*self.i
            try:
                widget.reajuste()
            except Exception:
                print("O widget não possui o método 'reajuste',caso esteja inserindo um widget provindo do kivy faça a herança e a adaptação em uma nova classe e implemente o método")

        self.layout.add_widget(widget)
        self.i+=1
    
    def clear(self):
        self.layout.clear_widgets()
        self.i = 0


class BlocoRolavel(RelativeLayout):
    """
        Esta classe tem como finalidade de criar um bloco na tela, onde os recursos fiquem armazenados 
        em uma forma geométrica, de maneira a organizar os dados e serem roláveis.

        A classe possui os seguintes parâmetros:
            - altura = altura da forma do bloco
            - largura = largura da forma do bloco
    """
    def __init__(self, width, height,pos_hint,spacing=10, **kwargs):
        super().__init__(**kwargs)
        
        self.width = width
        self.height = height
       
        # Adiciona um ScrollView à RelativeLayout
        self.scroll_view = ScrollView(size_hint=(None, None), size=(width, height),pos_hint=pos_hint)
        self.add_widget(self.scroll_view)
       
        # Cria um layout para armazenar os widgets dentro do ScrollView
        self.scrollable_layout = RelativeLayout(size_hint=(None, None), size=(width, height),pos_hint=pos_hint)
        self.scroll_view.add_widget(self.scrollable_layout)
       
        # Define o tamanho mínimo do ScrollView para mostrar a barra de rolagem
        self.scroll_view.bar_width = '10dp'
       
        # Configura a barra de rolagem para ocultar quando não for necessária
        self.scroll_view.bar_inactive_alpha = 0
        self.scroll_view.bar_color = [1, 1, 1, 0.8]
        self.scroll_view.effect_cls = 'ScrollEffect'
        self.total_height = self.height*2 + spacing
        self.spacing = spacing
        self.widgets = list()
       
    def add(self, widget):
        # Adiciona o widget ao layout scrollable_layout
        self.widgets.append(widget)
        self.__redefine_pos()
        self.total_height += widget.height + self.spacing
        self.scrollable_layout.height = max(self.total_height, self.height)

    def __redefine_pos(self):
        self.scrollable_layout.clear_widgets()
        total = self.total_height
        for widget in self.widgets:
            widget.pos[1] = total
            self.scrollable_layout.add_widget(widget)
            total -= widget.height + self.spacing
       
    def remove(self, widget):
        # Remove o widget do layout scrollable_layout
        self.total_height -= widget.height + self.spacing
        self.scrollable_layout.remove_widget(widget)
        self.scrollable_layout.height = max(self.total_height, self.height)
    
    def clearWidgets(self):
        self.total_height = 0
        self.scrollable_layout.clear_widgets()
        self.scrollable_layout.height = max(self.total_height, self.height)