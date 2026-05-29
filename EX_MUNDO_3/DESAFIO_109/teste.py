'''
Modifique as funções que foram criadas no DESAFIO 107, para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no DESAFIO 108.
'''

import moeda

i = input('Digite o preço: ').replace(',','.')
p = float(i)
print(f'A metade de {moeda.moeda(p)} é igual a {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.dobrar(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}')