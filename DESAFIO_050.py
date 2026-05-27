'''
Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o,
'''

print('Informe 6 números que irei somar todos os números pares que você digitar e dar o resultado.')
somapar = 0
for c in range (1, 7, 1):
    numero = int(input('{}° número: '.format(c)))
    if numero % 2 == 0:
        somapar = somapar + numero
print('A soma de todos os pares é {}.'.format(somapar))