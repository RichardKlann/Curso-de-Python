'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
ex: digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1

Tentar fazer isso como string e matemáticamente
'''

'''
#Método Matemático (que eu fiz)
print('Método matemático:')
numero = int(input('Digite um número entre 0 e 9999: '))
print('Unidade: {}'.format(numero%10))
numero = int((numero - numero%10)/10)
print('Dezena: {}'.format(numero%10))
numero = int((numero - numero%10)/10)
print('Centena: {}'.format(numero%10))
numero = int((numero - numero%10)/10)
print('Milhar: {}'.format(numero%10))
'''

#Método Matemático (que o curso apresentou)
print('Método matemático:')
numero1 = int(input('Digite um número entre 0 e 9999: '))
print('Unidade: {}'.format(numero1 % 10))
print('Dezena: {}'.format(numero1 // 10 % 10))
print('Centena: {}'.format(numero1 // 100 % 10))
print('Milhar: {}'.format(numero1 // 1000 % 10))

'''
#Não funciona para números menos que 1000
#Método String
print('\nMétodo String:')
numero = str(input('Digite um número entre 0 e 9999: '))
print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))
'''