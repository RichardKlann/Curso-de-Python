'''
Faça um programa que leia uma frase pelo teclado e mostre: 

Quantas vezes aparece a letra "A".
Em qual posição ela aparece a primeira vez
Em qual posição ela aparece a última vez
'''

frase = str(input('Escreva uma frase: '))
frase = frase.strip().upper()
print('A letra "A" aparece: {}'.format(frase.count('A')))
print('1a posição é: {}'.format(frase.find('A')))
print('última posição é: {}'.format(frase.rfind('A')))