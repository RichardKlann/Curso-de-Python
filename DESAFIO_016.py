'''
Crie um programa que leia um número real qualquer pelo teclado, e mostre na tela a sua porção inteira
ex: digite 6,127 e mostre somente a parte inteira 6
'''

#numero = float(input('Escreva qualquer número:'))
#print('A porção inteira deste número é: {:.0f}'.format(numero//1))

from math import floor
numero = float(input('Digite um número: '))
print('A parte inteira do número digitado é: {}'.format(floor(numero)))