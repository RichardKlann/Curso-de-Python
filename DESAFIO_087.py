'''
Aprimore o desafio anterior, mostrando no final: 

a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha
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

somapar = 0
for l in range (0, len(matriz)):
    for c in range (0, len(matriz[l])):
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]

print(f'a) A soma de todos os valores PARES da matriz é: {somapar}')

somac3 = 0
for l in range (0, len(matriz)):
    somac3 += matriz[l][2]
print(f'b) A soma de todos os valores da coluna 3 é igual a: {somac3}')

maiorl2 = max(matriz[1])
print(f'c) O maior valor da linha 2 é: {maiorl2}')