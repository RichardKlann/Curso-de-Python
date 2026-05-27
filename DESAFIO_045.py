'''
Crie um programa que faça o computador jogar JOKENPO com você
'''
from random import randint
from time import sleep

print ('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual a sua jogada?\n'))
if jogador > 2:
    print('OPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE!')
    quit()
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0,2)

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-' * 10)
print('Computador jogou {}'.format(opcoes[computador]))
print('Você jogou {}'.format(opcoes[jogador]))
print('=-' * 10)

if computador == jogador:
    print('EMPATE!')
elif computador == 0 and jogador == 1:
    print('JOGADOR VENCEU!')
elif computador == 0 and jogador == 2:
    print('COMPUTADOR VENCEU!')
elif computador == 1 and jogador == 0:
    print('COMPUTADOR VENCEU!')
elif computador == 1 and jogador == 2:
    print('JOGADOR VENCEU!')
elif computador == 2 and jogador == 0:
    print('JOGADOR VENCEU!')
elif computador == 2 and jogador == 1:
    print('COMPUTADOR VENCEU!')