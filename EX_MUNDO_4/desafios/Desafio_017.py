'''
Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também o método que mostre uma etiqueta de preço do produto.
'''
from rich import print
#from rich import inspect
from rich.panel import Panel 

class Produto:
    def __init__(self, nome, preco): #Método Construtor
        #Atributos de instância
        self.nome = nome
        self.preco = preco
    
    def __str__(self): #Ao definir esse ponto diferente, caso eu der um print direto print(p1), ele irá retornar a função que está abaixo, ao invés de toda a informação de qual posição da memória que está essa variável.
        return f"{self.nome} custa R${self.preco:,.2f}"

    #Métodos de instância
    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f'{"-" * 30}'
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel(conteudo, title="PRODUTO", width=34)
        print(etiqueta)

    
p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()