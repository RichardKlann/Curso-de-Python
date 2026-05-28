'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão.
'''

print ('=' * 25)
print ('10 TERMOS DE UMA PA'.center(25, ' ')) #Centraliza o texto
print ('=' * 25)
termo1 = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

for c in range (termo1, termo1 + 10, 1):
    print(termo1, end = ' -> ')
    termo1 = termo1 + razao
print('ACABOU!')