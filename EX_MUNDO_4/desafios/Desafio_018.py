'''
Crie uma classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve de ser comprado, o custo total do churrasco e o preço por pessoa.

400g de carne por pessoa
R$82,40 o Kg de carne
'''
from rich import print
from rich.panel import Panel

class Churrasco:
    #Atributos de classe
    consumo_padrao:float = 0.400 #Cada pessoa come em média 400g de carne
    preco_Kg:float = 82.40 #Cada Kg de carne custa R$82,40


    def __init__(self, titulo, qtdpessoas): #Método construtor
        #Atributos de instânica
        self.titulo = titulo
        self.qtdPessoas = int(qtdpessoas)


    def calcular_qtd_carne(self) -> float:
        return self.__class__.consumo_padrao * self.qtdPessoas


    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_Kg


    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.qtdPessoas

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.qtdPessoas} convidados[/]\n"
        conteudo += f"Cada participante comerá {self.__class__.consumo_padrao}Kg e cada Kg custa R${self.__class__.preco_Kg:.2f}\n"
        conteudo += f"Recomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne\n"
        conteudo += f"O custo total será de R${self.calcular_custo_total():.2f}\n"
        conteudo += f"Cada pessoa pagará R${self.calcular_custo_individual():.2f}"

        etiqueta = Panel(conteudo, title=self.titulo, width=70)
        print(etiqueta)


s1 = Churrasco("Churras dos amigos", 15)
s1.analisar()