'''
Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros elementos 
de uma sequência de fibonacci.

Ex:
0 - 1 - 1 - 2 - 3 - 5 - 8
'''

print('Irei te mostrar a sequência de fibonacci!')
n = int(input('Informe a quantidade de números da sequência que você quer: '))
n -= 2
num1 = 0
num2 = 1
print('\n', num1, '-', num2, '- ', end='')

while n > 0:
    soma = num1 + num2
    if n == 1:
        print(soma, end='')
    else:
        print(soma, end=' - ')
    num1 = num2
    num2 = soma
    n -= 1