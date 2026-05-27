'''
Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é par ou ímpar
'''

num = int(input('Escreva um número para que eu possa te falar se é par ou impar: '))

teste = num%2

if teste == 0:
    print('O número {} é par!'.format(num))

else:
    print('O número {} é ímpar!'.format(num))