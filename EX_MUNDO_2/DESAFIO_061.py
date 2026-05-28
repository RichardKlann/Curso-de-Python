'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos de uma progressão usando a estrutura while.
'''

ptermo = int(input('Informe o primeiro termo da razão: '))
razao = int(input('Informe a razão da PA: '))
c = 10

while c >= 0:
    if c != 0:
        print(ptermo, end = ' -> ')
        ptermo = ptermo + razao
    else:
        print(ptermo, end = '')
        ptermo = ptermo + razao
    c -= 1