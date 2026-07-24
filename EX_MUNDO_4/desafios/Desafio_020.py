'''
Crie uma classe chamada Gamer, onde podemos cadastrar o nome, nick, e os jogos favoritos de uma pessoa. 
Crie também o método que permita mostrar a ficha desse gamer.
'''
from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome Real: [black on white]  {self.nome}  [/]"
        conteudo += "\nJogos favoritos: "
        for jogo in self.favoritos:
            conteudo += f'\n{jogo}'
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)

j1 = Gamer("Fabrício da Silva", "Detonator2025")
j1.add_favoritos("Mário Bros.")
j1.add_favoritos("Battlefield 3")
j1.add_favoritos("CS-GO")
j1.ficha()


j2 = Gamer("Susana Sikoski", "Peach_Raivosa")
j2.add_favoritos("Canastra")
j2.add_favoritos("Jogo do Tigrinho")
j2.add_favoritos("Amarelinha")
j2.ficha()