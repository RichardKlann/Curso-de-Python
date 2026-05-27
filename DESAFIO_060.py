'''
Faça um programa que leia um número qualquer, e mostre o seu fatorial.

ex:
5! = 5x4x3x2x1 = 120
'''

numero = int(input('Informe o número para que eu lhe dê o seu fatorial: '))
fatorial = 1

print('Resultado de {}! = '.format(numero), end = '')

for c in range(numero, 0, -1):
    fatorial *= c
    print(c, end='')
    if c != 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(fatorial)




'''
numero = int(input('Informe o número para que eu lhe de o seu fatorial: '))
c = numero
resultado = 1

print('{}! = '.format(numero), end = '')
while c > 0:
    resultado = resultado * c
    print('{}'.format(c), end = '')
    if c != 1:
        print(' x ', end = '')
    c -= 1

print(' = {}'.format(resultado))
'''

    


'''
#IMPORTANDO BIBLIOTECA
from math import factorial

numero = input('Informe um número para eu lhe passar o valor fatorial dele: ')
teste = False

while teste == False:
    try:
        numero = int(numero)
        resultado = factorial(numero)
        teste = True
    except ValueError:
        print('\nDado inválido. Passe um número inteiro!')
        numero = input('\nInforme um número inteiro: ')

print('{}! = {}'.format(numero, resultado))'''