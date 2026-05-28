'''
Faça um programa que leia o comprimento do cateto oposto e do 
cateto adjacente de um triângulo retângulo
calcule e mostre a hipotenusa
'''

import math

CO = float(input('Informe o valor do Cateto Oposto: '))
CA = float(input('Informe o valor do Cateto Adjacente: '))

hipotenusa = math.hypot(CO, CA)

print('A hipotenusa é {:.1f}'.format(hipotenusa))