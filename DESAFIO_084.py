'''
Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final mostre:

a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves
'''

aux = []
pessoas = []

while True:
    aux.append(input('Nome: '))
    aux.append(int(input('Peso: ')))

    pessoas.append(aux[:])
    aux.clear()
    
    if input('Deseja continuar [S/N]? ') in 'nN':
        break

print(f'A quantidade de pessoas cadastradas foram: {len(pessoas)}')


maior = 0
for p in pessoas:
    if p[1] > maior:
        maior = p[1]

print(f'O maior peso foi de {maior}Kg com o nome de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]} ]', end='')

menor = 0
for p in pessoas:
    if menor == 0:
        menor = p[1]
    elif p[1] < menor:
        menor = p[1]

print()
print(f'O menor peso foi de {menor}Kg com o nome de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]} ]', end='')