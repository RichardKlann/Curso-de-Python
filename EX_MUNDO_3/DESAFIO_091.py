'''
Crie um programa onde 4 jogadores jogam um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6)}

ranking = {}

for k, v in jogo.items():
    sleep(1)
    print(f'O {k} jogou {v}')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('=-' * 30)
print('O Ranking dos jogadores é: ')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'    O {i+1}° Lugar foi o {v[0]} que tirou {v[1]}')