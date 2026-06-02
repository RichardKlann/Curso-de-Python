'''
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.

Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
'''

from utilidadecev import moeda

i = input('Digite o preço: ').replace(',','.')
p = float(i)
moeda.resumo(p, 30, 10)