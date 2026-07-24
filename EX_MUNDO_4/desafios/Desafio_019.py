'''
Crie uma classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.
'''

from rich import print
from rich import inspect
from time import sleep

class Livro:
    def __init__(self, titulo, paginas): #Método construtor
        #Atributos de instância
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red]{self.titulo}[/] que possui {self.total_paginas}", end="")
        print(f" [blue]páginas no total. Você agora está na [yellow]página {self.pagina_atual}")

    #Métodos de instância
    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward:", end=" ")
                sleep(0.2)
                cont += 1
        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][/blue]")
        if self.fim_do_livro():
            print(f':closed_book: [red]Você chegou a o final do livro "{self.titulo}"[/red]')

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False
        "return True if self.pagina_atual == self.total_paginas else False"


        




l1 = Livro("10 coisas que aprendi na vida", 20)


l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(20)
