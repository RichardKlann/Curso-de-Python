'''
Crie uma classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.
'''

from rich import print
from rich import inspect

class Livro:

    def __init__(self, titulo, qtd_pag, pagina_atual=1): #Método construtor
        #Atributos de instância
        self.titulo = titulo
        self.qtd_pag = qtd_pag
        self.pagina_atual = pagina_atual
        print(f"Você acabou de abrir o livro '{self.titulo}' que possui {self.qtd_pag} páginas")
        print(f"Você agora está na página n° {self.pagina_atual}")

    def __str__(self) -> str:
        return f"Título: {self.titulo}\nQuantidade de páginas {self.qtd_pag}"

    #Métodos de instância
    def avancar_paginas(self, qtd_pag_avanca=0):
        while True:
            for c in range(0, qtd_pag_avanca, 1):
                if self.pagina_atual <= self.qtd_pag:
                    print(f"Pág{self.pagina_atual}", end="")
                    self.pagina_atual += 1
                    if c < qtd_pag_avanca:
                        print(" -> ", end="")                    
            break


l1 = Livro("10 coisas que aprendi na vida", 30)


l1.avancar_paginas(5)
l1.avancar_paginas(3)



#paginit = 1
#for c in range(1, 5, 1):
#    print(f"Pág{c} -> ", end="")