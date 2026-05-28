'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior. Os dois são iguais
'''

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if num1 > num2:
    print('{} é maior que {}.'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}.'.format(num2, num1))
else:
    print('Ambos os números são iguais!')