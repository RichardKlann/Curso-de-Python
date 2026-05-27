'''
Faça um programa que leia um ângulo qualquer e mostre na tela 
o valor do seno, cosseno e tangente desse ângulo
'''
import math

angulo = float(input('Informe o valor do ângulo em graus: '))
angulo = math.radians(angulo)

sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print(f'Seno: {sen:.2f}')
print(f'Cosseno: {cos:.2f}')
print(f'Tangente: {tan:.2f}')
