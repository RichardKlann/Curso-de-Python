'''
Crie uma classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.
'''

from rich import print
from rich import inspect
from time import sleep

class Livro:

    def __init__(self, titulo, qtd_pag, pagina_atual=1): #Método construtor
        #Atributos de instância
        self.titulo = titulo
        self.qtd_pag = qtd_pag
        self.pagina_atual = pagina_atual
        print(f"Você acabou de abrir o livro '[red]{self.titulo}[/]' que possui [green]{self.qtd_pag} páginas[/] no total.", end=" ")
        print(f"Você agora está na [yellow]página n° {self.pagina_atual}[/].")

    def __str__(self) -> str:
        return f"Título: {self.titulo}\nQuantidade de páginas {self.qtd_pag}"

    #Métodos de instância
    def avancar_paginas(self, qtd_pag_avanca=0):
            if (qtd_pag_avanca + self.pagina_atual) > self.qtd_pag:
                qtd_pag_avanca = self.qtd_pag
            cont = 1
            while cont <= qtd_pag_avanca:
                if self.pagina_atual != self.qtd_pag:
                    self.pagina_atual += 1
                    print(f"Pág.{self.pagina_atual}", end="")
                    if cont != qtd_pag_avanca:
                        print(" -> ", end="")
                        sleep(0.5)
                    else:
                        print(f"\nVocê avançou {qtd_pag_avanca} páginas e agora está na página {self.pagina_atual}.")
                    cont += 1
                    if self.pagina_atual == self.qtd_pag:
                        print("Você chegou ao final do livro!")
                         
                else:
                     print("Você chegou ao final do livro!")
                     break
                     





l1 = Livro("10 coisas que aprendi na vida", 30)


l1.avancar_paginas(18)
l1.avancar_paginas(10)
l1.avancar_paginas(4)
