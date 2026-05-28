'''
Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e os valores ímpares. No final mostre o valores
pares e ímpares em ordem crescente.
'''
            #par    #impar
numeros =   [[],    []]


for c in range (0, 7):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 != 0:
        numeros[1].append(valor)

print('=-' * 30)

numeros[0].sort()
numeros[1].sort()

print(f'Todos os valores pares digitados foram: {numeros[0]}')
print(f'Todos os valores ímpares digitados foram: {numeros[1]}')

print(numeros)

