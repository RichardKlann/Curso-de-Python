'''
Aprimore o DESAFIO 93, para que ele funcione com vários jogadores,
Incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
'''
from time import sleep

estatjogador = list()
dados = {} #nome, gols/partida, total de gols
gols = []

while True: #Entrada dos dados
    dados['jogador'] = str(input('Nome do jogador: '))

    qtdpartidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))

    for c in range(0,qtdpartidas):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))

    dados['gols'] = gols[:]
    gols.clear()

    total = 0
    for c in dados['gols']:
        total += c
    dados["total"] = total
    estatjogador.append(dados.copy())

    resp = str(input('Deseja adicionar mais jogadores [S/N]? ')).strip()[0].upper()
    if resp in 'Nn':
        break


while True:
    print('=' * 30)
    print()
    print('Jogadores cadastrados: ')
    for i, e in enumerate(estatjogador):
        print(f'{i:<3}', '.'*3 , f'  {e["jogador"]}')
    print('=' * 30)
    
    while True:
        print()
        escolha = int(input('Informe o número do jogador que deseja ver as estatísticas: '))
        if escolha not in range (0, len(estatjogador)):
            print('Número inválido... Tente novamente...')
            sleep(1)
            break

        print(f'O jogador {estatjogador[escolha]["jogador"]} jogou {len(estatjogador[escolha]["gols"])} partidas.')
        for i, v in enumerate(estatjogador[escolha]['gols']):
            print(f'Na partida {i}, fez {v} gols...')

        resp = str(input('Deseja encerrar o programa [S/N]? ')).strip().upper()[0]
        if resp in 'Ss':
            break
    if resp in 'Ss':
        break

print('ENCERRANDO PROGRAMA...')
sleep(1)

    #O jogador X fez jogou tantas partidas.
    #Na partida x, fez y gols...
