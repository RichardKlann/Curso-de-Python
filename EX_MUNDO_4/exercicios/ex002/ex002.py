#Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use
    variável = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): #Método Construtor
        #Atributos de instância
        self.nome = nome
        self.idade = idade

    #Métodos de instância
    def aniversário(self):
        self.idade = self.idade + 1


    def __str__(self): #Dunder method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    

    def __getstate__(self): #
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

#Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversário()
print(g1)

g2 = Gafanhoto("Mauro", 53)
g2.aniversário()
print(g2)

g3 = Gafanhoto()
print(g3)

print(Gafanhoto.__doc__) #MOSTRA A DOCUMENTAÇÃO QUE FOI ESCRITA
print(g1.__dict__) #MOSTRA O DICIONÁRIO QUE ESTÁ SALVO NA MEMÓRIA - ATRIBUTO
print(g1.__getstate__()) #FAZ A MESMA COISA QUE __DICT__ - MÉTODO - ESSE MÉTODO PODE SER PERSONALIZADO DA MESMA FORMA COMO FOI FEITO O __str__

print(g1.__class__) #MOSTRA DE QUAL CLASSE QUE É ESSE OBJETO