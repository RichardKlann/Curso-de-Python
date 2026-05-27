'''
Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e qual foi o menor
peso lido.
'''

maior = menor = 0

peso = float(input('Informe o peso da pessoa n° 1: '))
maior = menor = peso
for c in range(2, 6, 1):
    peso = float(input('Informe o peso da pessoa n° {}: '.format(c)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('De todos os pesos informados o menor é {:.1f}Kg, e o maior é {:.1f}Kg'.format(menor, maior))













'''
peso = [0, 0, 0, 0, 0]
for c in range (1, 6):
    peso[c-1] = float(input('Informe o peso: '))
    print(peso[c-1])


maior = max(peso)
menor = min(peso)
print('De todos os pesos lidos o maior foi {} e o menor foi {}.'.format(maior, menor))



"""
maior = peso[0]
for c in range (0, 4):
    if peso[c+1] > maior:
        maior = peso[c+1]

print(maior)


menor = peso[0]
for c in range (0, 4):
    if peso[c+1] < menor:
            menor = peso[c+1]

print(menor)"""

'''