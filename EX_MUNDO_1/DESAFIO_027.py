'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
Ex: Ana Maria de Souza
Primeiro: Ana
Último: Souza
'''

nome = str(input('Informe o seu nome completo: ').split())

divisao = nome.split()

print('Primeiro nome: {}'.format(divisao[0]))
print('Último nome: {}'.format(divisao[len(divisao)-1]))