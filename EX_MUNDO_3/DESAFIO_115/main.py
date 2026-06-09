'''
Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo simples.

O sistema só vai ter duas opções:
Cadastrar uma nova pessoa.
Listar todas as pessoas cadastradas
'''

import funcoes115

loop = True
while True:
    funcoes115.showMenu()
    loop = funcoes115.userEnterOption()
    if loop == False:
        break