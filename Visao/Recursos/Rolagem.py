from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout

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
            - spacing = espaçamento entre os widgets (Por padrão vem em 100%)
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

                rolagem = caixaRolagem([bloco])

        OBS: Somente os widgets que forem adicionados a essa caixa de rolagem, vão ter a capacidade de serem listados e movidos pela barra.
        Caso insira essa caixa de rolagem em um outro layout com widgets fixos, os mesmos não irão se mover
    """
    def __init__(self,listaWidgets:list,cols=1,spacing=0.4,row_default_height=500,padding=100,col_default_width=100,**kwargs):
        super().__init__(**kwargs)

        scroll = ScrollView()


        layout = GridLayout(cols=cols,size_hint_y=None,row_force_default=True,row_default_height=row_default_height,col_default_width=col_default_width,padding=padding)
        layout.bind(minimum_height = layout.setter('height'))

        i = 0
        for widget in listaWidgets:
            if i > 0:
                widget.pos_hint['center_y'] += spacing*i
                try:
                    widget.reajuste(spacing)
                except Exception:
                    print("O widget não possui o método 'reajuste',caso esteja inserindo um widget provindo do kivy faça a herança e a adaptação em uma nova classe e implemente o método")

            layout.add_widget(widget)
            i+=1

        scroll.bar_width = 10
        scroll.add_widget(layout)
        self.add_widget(scroll)
