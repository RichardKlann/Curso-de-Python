'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valor lido. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''


loop = True

num = int(input('Digite um número: '))
maior = num
menor = num
media = num
cont = 1

continua = str(input('Quer continuar? [S/N] '))
if continua in 'Nn':
    loop = False

while loop == True:
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    media += num
    cont += 1

    continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        loop = False

print('MAIOR = {}'.format(maior))
print('MENOR = {}'.format(menor))
print('MÉDIA = {}'.format(media/cont))
