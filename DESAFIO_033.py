'''
Faça um programa que leia 3 números, e mostre qual é o maior e qual é o menor
'''

n1 = int(input('Informe o 1° número: '))
n2 = int(input('Informe o 2° número: '))
n3 = int(input('Informe o 3° número: '))

#Teste do maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#Teste do menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('Entre os 3 números digitados, o menor e o maior número digitados respectivamente são {} e {}'.format(menor, maior))