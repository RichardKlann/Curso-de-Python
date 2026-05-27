'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o 
total de gols feitos durante o campeonato.
'''
dados = {}
gols = []

dados['jogador'] = str(input('Nome do jogador: '))
qtdpartidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))

for c in range(0,qtdpartidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))

dados['gols'] = gols[:]

total = 0
for c in dados['gols']:
    total += c
dados["total"] = total

print('=-' * 30)
print(dados)
print('=-' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)

print(f'O jogador {dados["jogador"]} jogou {qtdpartidas} partidas.')
for n, g in enumerate(dados['gols']):
    print(f'--> Na partida {n}, fez {g} gols')