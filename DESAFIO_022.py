'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar os espaços)
- Quantas letras tem o primeiro nome?
'''

nome = str(input('Digite seu nome completo: '))
print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras úteis: {}'.format(len(nome.strip()) - nome.count(' ')))
divisao = nome.split()
print('Seu primeiro nome é {} e a quantidade de letras dele é {}'.format(divisao[0], len(divisao[0])))