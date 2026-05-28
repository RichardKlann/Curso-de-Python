'''
Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(largura, comprimento):
    calculo = largura * comprimento
    print(f'A largura é {largura} e o comprimento é {comprimento}')
    print(f'A área total do terreno é {calculo:.2f}m²')


a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)
