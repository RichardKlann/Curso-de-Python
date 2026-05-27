'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados de forma tabular.
'''

listagem = ('Borracha', 1.75,
            'Caneta', 2.00,
            'Caderno', 15.00,
            'Folhas A4', 14.99,
            'Livro Matemática', 74.95)


print('-' * 60)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print('-' * 60)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<50}', end = '')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 60)