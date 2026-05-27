'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
'''
#Funções
def ficha(nome='', numgols=''):
    print('-' * 30)
    nome = str(input('Nome do jogador: '))
    if nome.strip() == '':
        nome = '<desconhecido>'
    numgols = input('Número de gols: ')
    if numgols.isnumeric():
        int(numgols)
    else:
        numgols = 0
    print(f'O jogador {nome} fez {numgols} gol(s) no campeonato')

ficha()