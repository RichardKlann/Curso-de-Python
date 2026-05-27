'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matríz na tela, com a formatação correta.
'''
        #    0       1       2
matriz =    [[],    [],     []]

for l in range (0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('=-' * 40)

for p in range (0, len(matriz)):
    for i in range (0, len(matriz[p])):
        print(f'[ {matriz[p][i]:^5} ]', end ='')
    print()
