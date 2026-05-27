'''
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador

O programa deverá escrever na tela do usuário se o usuário venceu ou perdeu! 
'''

from random import randint
from time import sleep

computador = randint(0 , 5) #Computador "Pensa" em um número entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em qual número pensei? ')) #Jogador tenta adivinhar o número
print('PROCESSANDO...')
sleep(2)

if computador == jogador:
    print('Parabéns você acertou o número!')

else:
    print('Errou! O número escolhido era {}.'.format(computador))