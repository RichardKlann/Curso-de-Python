'''
Adapte o código do DESAFIO 107, criando uma função adicional chamada moeda que consiga mostrar os valores como valor monetário formatado.
'''

import moeda

i = input('Digite o preço: ').replace(',','.')
p = float(i)
print(f'A metade de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.dobrar(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')