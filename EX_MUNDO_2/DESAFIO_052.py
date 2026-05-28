'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
(número que são divisíveis somente por 1 e por ele mesmo.)
'''

numero = int(input('Digite um número inteiro: '))
contagem = 0

for c in range (1, numero+1, 1):
    if numero % c == 0:
        contagem += 1
        print('O número {} é divisível por {}'.format(numero, c))
if contagem == 2:
    print('Portanto, o número {} é um número primo!'.format(numero))
else:
    print('Portanto, o número {} não é um número primo!'.format(numero))