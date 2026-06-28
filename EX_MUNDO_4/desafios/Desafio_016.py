'''
Crie uma classe Funcionário, onde podemos cadastrar nome, setor e cargo.
Crie também um método que permita o funcionário se apresentar.
'''

from rich import print
from rich import inspect

class Funcionario:
    '''Cria um funcionário com 3 argumentos distintos - nome, setor e cargo'''
    #Atributos de classe - é para todas as instâncias criadas (em comum)
    empresa = "RAK Engenharia"

    def __init__(self, nome, setor, cargo): #Método construtor
        #Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    #Métodos de instância
    def apresentacao(self) -> str:
        '''Mostra na tela uma mensagem de apresentação do funcionário, contendo nome, setor e cargo na empresa.'''

        return f":handshake: Olá, eu sou [bold blue]{self.nome}[/] e sou [bold blue]{self.cargo}[/] do setor [bold blue]{self.setor}[/] na empresa {self.__class__.empresa}."
    
f1 = Funcionario("Richard", "Qualidade", "Técnico em eletrônica")
f2 = Funcionario("Susana", "Limpeza", "Supervisora de equipe")

#inspect(f1, methods=True, dunder=True)
print(f1.apresentacao())
print(f2.apresentacao())