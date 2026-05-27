'''

Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador

O programa deverá escrever na tela do usuário se o usuário venceu ou perdeu! 



Melhore o jogo do desafio 028, onde o computador vai pensar em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''

from random import randint

palpite = 0
esccomp = escjog = ''
esccomp = randint(0, 10)

escjog = input('Pensei em um número de 0 até 10. Tente adivinhar: ')
if escjog == '':
    print('Você precisa digitar algo!')
    palpite -= 1
else:
    escjog = int(escjog)

if escjog == esccomp:
    palpite = 1

while escjog != esccomp:
    palpite += 1
    escjog = input('Você errou o palpite n° {}. Tente novamente: '.format(palpite))
    if escjog == '':
        print('Você precisa digitar algo!')
        palpite -= 1
    else: 
        escjog = int(escjog)


print('Parabéns, você acertou o número que escolhi, {}. ' \
'Você realizou {} palpites para acertar!'.format(esccomp, palpite))

