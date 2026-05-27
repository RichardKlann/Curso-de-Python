'''
Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome escolhido
'''

from random import choice

n1 = str(input('1° nome: '))
n2 = str(input('2° nome: '))
n3 = str(input('3° nome: '))
n4 = str(input('4° nome: '))

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('Quem irá apagar o quadro será: {}.'.format(escolhido))