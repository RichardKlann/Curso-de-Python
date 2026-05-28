'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1, 60 para cada jogo, cadastrando tudo em uma lista composta.

Usar um timer de 1s para cada jogo que for sorteado e aparecendo para o usuário.
'''

from random import randint
from time import sleep

jogos = []
aux = []


qtdjogos = int(input('Deseja quantos palpites? '))
n = 0
for qtd in range (0, qtdjogos):
    while n != qtdjogos:
        for c in range(0, 6):
            num = randint(1, 60)
            if num in aux:
                aux.clear()
                break
            aux.append(num)
        if aux != []:
            jogos.append(aux[:])
            aux.clear()
            n +=1

i = 0
for p in jogos:
    sleep(1)
    print(f'Palpite n° {i+1}: {jogos[i]}')
    i += 1