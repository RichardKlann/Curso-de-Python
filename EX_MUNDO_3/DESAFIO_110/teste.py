'''
Adicione ao módulo moeda.py criado nos desafios anteriores uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
'''

import moeda

i = input('Digite o preço: ').replace(',','.')
p = float(i)
moeda.resumo(p, 30, 10)