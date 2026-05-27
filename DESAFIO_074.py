'''
Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), 
           randint(1,10), randint(1,10))

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

#Método inteligente:
print(numeros)
print(f'O maior valor é: {max(numeros)}')
print(f'O menor valor é: {min(numeros)}')


#Método desenvolvido
'''
print(numeros)
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
'''