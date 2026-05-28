'''Programa que leia um número inteiro qualquer
e mostre na tela a sua tabuada
'''

'''Tentativa 1
numero = int(input('Digite um número para que eu lhe informa a tabuada de 0 até 10: '))
print('{}x0 = {}'.format(numero, numero*0))
print('{}x1 = {}'.format(numero, numero*1))
print('{}x2 = {}'.format(numero, numero*2))
print('{}x3 = {}'.format(numero, numero*3))
print('{}x4 = {}'.format(numero, numero*4))
print('{}x5 = {}'.format(numero, numero*5))
print('{}x6 = {}'.format(numero, numero*6))
print('{}x7 = {}'.format(numero, numero*7))
print('{}x8 = {}'.format(numero, numero*8))
print('{}x9 = {}'.format(numero, numero*9))
print('{}x10 = {}'.format(numero, numero*10))
'''
num = int(input('Digite um número e tenha a sua tabuada: '))
print('=' * 12)
print('{} x {:2} = {}'.format(num, 0, num*0))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('=' * 12)

#Adicionar {:2} indica que deve de ser impresso com apenas espaços...
#Adicionar {:.2f} indica que deve de ser impresso apenas duas casas decimais após a vírgula...