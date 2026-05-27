'''Faça um algoritmo que leia
o preço de um produto e mostre
seu novo preço com 5% de desconto'''

preco = float(input('Informe o preço do produto: R$'))
print('O novo preço do produto considerando um desconto de 5% é R${:.2f}'.format(preco*0.95))